#!/data/data/com.termux/files/usr/bin/bash

# Local-only incident evidence collector for Android Termux.
# It does not scan, contact, block, or disrupt any remote system.
set -u
set -o pipefail

readonly MAX_ARCHIVE_BYTES=$((100 * 1024 * 1024))
readonly SNAPSHOT_LIMIT=$((512 * 1024))
readonly STATIC_LIMIT=$((5 * 1024 * 1024))
readonly MINUTES="${1:-10}"

if [[ "$MINUTES" != "5" && "$MINUTES" != "10" ]]; then
  echo "Usage: $0 [5|10]" >&2
  exit 64
fi

readonly STARTED_AT="$(date -u +%Y%m%dT%H%M%SZ)"
readonly OUTPUT_ROOT="${HOME}/incident-evidence"
readonly EVIDENCE_DIR="${OUTPUT_ROOT}/incident-${STARTED_AT}"
readonly ARCHIVE="${OUTPUT_ROOT}/incident-${STARTED_AT}.tar.gz"
readonly INTERVAL=60
readonly SNAPSHOTS=$((MINUTES * 60 / INTERVAL))

mkdir -p "$EVIDENCE_DIR"
umask 077

capture() {
  local name="$1"
  local limit="$2"
  shift 2
  local destination="${EVIDENCE_DIR}/${name}"
  local temporary="${destination}.tmp"

  {
    printf 'collected_at_utc=%s\n\n' "$(date -u +%FT%TZ)"
    "$@"
  } >"$temporary" 2>&1 || true
  head -c "$limit" "$temporary" >"$destination"
  rm -f "$temporary"
}

capture_proc_file() {
  local name="$1"
  local path="$2"
  capture "$name" "$STATIC_LIMIT" cat "$path"
}

{
  printf 'collection_started_utc=%s\n' "$(date -u +%FT%TZ)"
  printf 'duration_minutes=%s\n' "$MINUTES"
  printf 'scope=local_device_only\n'
  printf 'network_activity=passive_observation_only\n'
} >"${EVIDENCE_DIR}/manifest.txt"

capture "system.txt" "$STATIC_LIMIT" uname -a
capture "termux-info.txt" "$STATIC_LIMIT" termux-info
capture_proc_file "processes.txt" "/proc/1/status"
capture_proc_file "tcp-initial.txt" "/proc/net/tcp"
capture_proc_file "tcp6-initial.txt" "/proc/net/tcp6"
capture_proc_file "udp-initial.txt" "/proc/net/udp"
capture_proc_file "udp6-initial.txt" "/proc/net/udp6"

for ((snapshot = 1; snapshot <= SNAPSHOTS; snapshot++)); do
  capture "snapshot-${snapshot}-tcp.txt" "$SNAPSHOT_LIMIT" cat "/proc/net/tcp"
  capture "snapshot-${snapshot}-tcp6.txt" "$SNAPSHOT_LIMIT" cat "/proc/net/tcp6"
  capture "snapshot-${snapshot}-udp.txt" "$SNAPSHOT_LIMIT" cat "/proc/net/udp"
  capture "snapshot-${snapshot}-processes.txt" "$SNAPSHOT_LIMIT" ps -ef
  [[ "$snapshot" -lt "$SNAPSHOTS" ]] && sleep "$INTERVAL"
done

(
  cd "$OUTPUT_ROOT"
  tar -czf "$ARCHIVE" "$(basename "$EVIDENCE_DIR")"
)

if [[ "$(wc -c <"$ARCHIVE")" -gt "$MAX_ARCHIVE_BYTES" ]]; then
  rm -f "$ARCHIVE"
  printf 'Archive exceeded the 100 MiB limit; retained evidence directory: %s\n' "$EVIDENCE_DIR" >&2
  exit 1
fi

sha256sum "$ARCHIVE" >"${ARCHIVE}.sha256"
printf 'Evidence archive created: %s\nSHA-256: %s\n' "$ARCHIVE" "$(cut -d' ' -f1 "${ARCHIVE}.sha256")"
