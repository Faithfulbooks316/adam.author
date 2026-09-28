# adam.author

## Termux incident evidence collector

`scripts/anti-hacker.sh` is a local-only, passive evidence collector for an Android device running Termux. It records limited snapshots of the device's own process and socket tables for either five or ten minutes, then creates a SHA-256-verified archive capped at 100 MiB.

It does not scan, contact, block, or disrupt remote systems, and it cannot guarantee protection against attacks. For hosted-site protection, configure rate limiting and DDoS controls through the hosting provider.

In Termux:

```sh
pkg install bash coreutils tar
chmod +x scripts/anti-hacker.sh
./scripts/anti-hacker.sh 10
```

Archives are written under `~/incident-evidence`. Run it only on a device and account you administer. To attach it to an Android home-screen shortcut, use the Termux:Widget app and place a launcher script there that invokes this script.