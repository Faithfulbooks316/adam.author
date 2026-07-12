"""
Gods of the Nations — Sales Page Generator
Author: Adam Joseph Hanrahan / FaithfulBooks Publishing
---
Run:  python3 build_sales_page.py
Out:  gods_of_nations_sales_page.html  (open in any browser or host anywhere)

Gumroad workflow:
  1. Run this script → get the .html file
  2. Host on your own domain, GitHub Pages, Netlify, or Carrd (custom embed)
  3. Paste that URL into your Gumroad product description or "Custom URL" field
"""

from pathlib import Path
from textwrap import dedent

# ──────────────────────────────────────────────
#  BOOK DATA  (edit here to update the page)
# ──────────────────────────────────────────────
BOOK = {
    "title":       "Gods of the Nations",
    "subtitle":    "How Non-Abrahamic Traditions Expose the Global Reality of Demonic Warfare",
    "author":      "Adam Joseph Hanrahan",
    "publisher":   "FaithfulBooks Publishing",
    "pages":       198,
    "gumroad_url": "https://adamhanrahan.gumroad.com",
    "kofi_url":    "https://ko-fi.com/adamhanrahan",
    "google_play": "https://play.google.com/store/books/details?id=7SybEQAAQBAJ",
    "site_url":    "https://www.faithfulbooks.carrd.co",
    "email":       "faithfulbookspublishing@outlook.com",
}

# ──────────────────────────────────────────────
#  SERIES / UPSELL DATA
# ──────────────────────────────────────────────
SERIES = [
    {
        "num":   "Book 1 · Soul Cage Series",
        "title": "Shattering the Veil: The Reality of Spiritual Warfare",
        "desc":  (
            "The foundational Spiritual Giant playbook. Hanrahan maps three battlegrounds "
            "—cosmic, cultural, and personal— and documents the observable 6 stages of demonic "
            "attack: Invitation → Infiltration → Oppression → Obsession → Possession → Death. "
            "Where <em>Gods of the Nations</em> shows you the enemy's history, "
            "<em>Shattering the Veil</em> puts weapons in your hands."
        ),
        "url":   "https://adamhanrahan.gumroad.com",
        "cta":   "Get Book 1 →",
    },
    {
        "num":   "Book 2 · Soul Cage Series — Only $0.99",
        "title": "Demonic Origins: Ancient Roots of Mankind's Spiritual War",
        "desc":  (
            "Drawing from the Books of Enoch, Jubilees, Solomon, Ezekiel, Genesis, "
            "Revelation, and The Life of Adam &amp; Eve, Hanrahan constructs the definitive "
            "genealogy of mankind's natural enemy — their motives, strengths, "
            "weaknesses, and the mechanics of the coming beast system. "
            "The intelligence brief every spiritual warrior needs."
        ),
        "url":   "https://play.google.com/store/books/details?id=7SybEQAAQBAJ",
        "cta":   "Get Book 2 — $0.99 →",
    },
    {
        "num":   "Book 3 · Soul Cage Series",
        "title": "Soul Cage: The Return of the Ancient Demonic",
        "desc":  (
            "A live war report. From the charred infant remains at Carthaginian Tophets "
            "to CERN's 12-ft Shiva statue, the Bohemian Grove rituals, and the post-1940s "
            "resurgence of pharmekia and forbidden knowledge — Hanrahan lays out how the "
            "fallen are moving into position <em>right now</em>. "
            "The most urgent book in the series."
        ),
        "url":   "https://adamhanrahan.gumroad.com",
        "cta":   "Get Book 3 →",
    },
]

# ──────────────────────────────────────────────
#  TRADITIONS / INSIDE-THE-BOOK CARDS
# ──────────────────────────────────────────────
TRADITIONS = [
    {
        "icon":  "𒀭",   # cuneiform divine determinative
        "name":  "Ancient Mesopotamia",
        "body":  (
            "The oldest exorcism texts in human history. The <em>gallu</em>, "
            "<em>Lamashtu</em>, and the demonic hierarchy Sumerian priests mapped "
            "with clinical precision — and the elaborate ritual warfare required to survive them."
        ),
    },
    {
        "icon":  "☽",
        "name":  "Zoroastrianism",
        "body":  (
            "The first fully developed cosmic dualism on record. Angra Mainyu leads an "
            "organized adversarial empire whose administrative structure maps onto modern "
            "systems of control with disturbing accuracy. Discover why Zoroaster reads "
            "like a 21st-century whistle-blower."
        ),
    },
    {
        "icon":  "𓂀",   # eye of Ra
        "name":  "Ancient Egypt",
        "body":  (
            "Apep — the chaos serpent who attacks the solar barque of Ra every single night. "
            "Why Egyptian priests conducted daily ritual warfare against this entity "
            "as a matter of cosmic survival, and what <em>Ma'at</em> reveals about "
            "the spiritual architecture of civilization itself."
        ),
    },
    {
        "icon":  "ᚠ",   # Norse rune
        "name":  "Norse Cosmology",
        "body":  (
            "The most brutally honest tradition in history: one that acknowledges its "
            "adversarial forces will ultimately win at Ragnarök — and declares that "
            "fighting anyway is the only worthy human response. "
            "A cosmology for warriors who refuse to quit."
        ),
    },
    {
        "icon":  "⊕",
        "name":  "Gnosticism & the Archons",
        "body":  (
            "The most radical adversarial cosmology ever constructed. The material world "
            "itself as a prison built by flawed, malevolent Archons — cosmic administrators "
            "of ignorance. The Gnostic liberation manual reads like an escape plan "
            "from a spiritual surveillance state."
        ),
    },
    {
        "icon":  "ॐ",
        "name":  "Hindu & Buddhist Traditions",
        "body":  (
            "The <em>Asuras</em>, <em>Mara</em>, and the East's great contribution: "
            "the most dangerous adversarial force has already infiltrated consciousness. "
            "The internal battlefield where the real war is won — or permanently lost."
        ),
    },
]

# ──────────────────────────────────────────────
#  THREE COSMOLOGICAL MODELS
# ──────────────────────────────────────────────
MODELS = [
    {
        "roman": "I",
        "name":  "Chaos vs. Order",
        "desc":  "Egypt, Mesopotamia, Norse — adversarial force as the primordial void pressing against the fragile achievement of creation. The enemy doesn't hate you; it simply predates you.",
    },
    {
        "roman": "II",
        "name":  "Cosmic Dualism",
        "desc":  "Zoroastrianism, Manichaeism — reality divided between two fundamental principles with human beings as the battlefield. Every moral choice is a vote cast in a war of cosmic magnitude.",
    },
    {
        "roman": "III",
        "name":  "Entrapment Cosmologies",
        "desc":  "Gnosticism, Buddhism, Mandaeanism — consciousness itself imprisoned by forces that profit from its ignorance. The path is not battle but awakening: gnosis over conquest.",
    },
]

# ──────────────────────────────────────────────
#  PAGE BUILDER FUNCTIONS
# ──────────────────────────────────────────────

def css() -> str:
    """Return the complete CSS block — glossy black + blood red design system."""
    return dedent("""
    /* ═══════════════════════════════════════════
       DESIGN TOKENS
    ═══════════════════════════════════════════ */
    :root {
      /* Reds */
      --blood:      #7B0000;
      --crimson:    #A31515;
      --fire:       #D63031;
      --ember:      #E17055;

      /* Blacks / surfaces */
      --void:       #000000;
      --gloss:      #080808;
      --jet:        #0F0F0F;
      --obsidian:   #161616;
      --slate:      #1E1E1E;
      --smoke:      #2A2A2A;

      /* Text */
      --parchment:  #EDE0C4;
      --silver:     #B8B8B8;
      --ash:        #707070;

      /* Accents */
      --gold:       #C9A84C;
      --gold-hi:    #E8C96A;

      /* Gloss sheen tint */
      --sheen:      rgba(255,255,255,0.03);
    }

    /* ═══════════════════════════════════════════
       RESET
    ═══════════════════════════════════════════ */
    *, *::before, *::after { margin:0; padding:0; box-sizing:border-box; }
    html { scroll-behavior:smooth; font-size:17px; }

    body {
      background: var(--void);
      color: var(--silver);
      font-family: 'Cormorant Garamond', Georgia, 'Times New Roman', serif;
      line-height: 1.8;
      overflow-x: hidden;
    }

    /* ── Glossy black paint effect ── */
    body::before {
      content:'';
      position:fixed; inset:0; pointer-events:none; z-index:0;
      background:
        /* Red atmospheric glow — top-left */
        radial-gradient(ellipse 60% 50% at 0% 0%,
          rgba(123,0,0,.18) 0%, transparent 70%),
        /* Red atmospheric glow — bottom-right */
        radial-gradient(ellipse 60% 50% at 100% 100%,
          rgba(123,0,0,.14) 0%, transparent 70%),
        /* Glossy sheen — top */
        linear-gradient(180deg,
          rgba(255,255,255,.055) 0%,
          rgba(255,255,255,.01) 18%,
          transparent 40%),
        /* Subtle scan-line depth */
        repeating-linear-gradient(
          180deg,
          transparent 0px, transparent 3px,
          rgba(255,255,255,.008) 3px, rgba(255,255,255,.008) 4px
        );
    }

    /* ── Noise grain overlay ── */
    body::after {
      content:'';
      position:fixed; inset:0; pointer-events:none; z-index:0;
      opacity:.4;
      background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='.9' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)' opacity='.06'/%3E%3C/svg%3E");
    }

    /* All real content sits above fixed pseudo-elements */
    .layer { position:relative; z-index:1; }

    /* ═══════════════════════════════════════════
       TYPOGRAPHY
    ═══════════════════════════════════════════ */
    h1, h2, h3 {
      font-family: 'Trajan Pro 3', 'Cormorant SC', 'Cinzel', Georgia, serif;
      font-weight: 700;
      letter-spacing: .04em;
      line-height: 1.1;
    }
    h4, h5, .eyebrow, .label-tag, nav, .stat-label, .card-name,
    .model-roman, .btn, .badge {
      font-family: 'Cormorant SC', 'Cinzel', Georgia, serif;
      letter-spacing: .14em;
    }

    em   { color: var(--gold-hi); font-style: italic; }
    strong { color: var(--parchment); }
    a    { color: var(--fire); text-decoration: none; transition: color .2s; }
    a:hover { color: var(--gold-hi); }

    /* ═══════════════════════════════════════════
       NAV
    ═══════════════════════════════════════════ */
    nav {
      position:sticky; top:0; z-index:200;
      display:flex; align-items:center; justify-content:space-between;
      padding: 13px 48px;
      background: rgba(8,8,8,.95);
      backdrop-filter: blur(20px) saturate(1.4);
      border-bottom: 1px solid rgba(123,0,0,.4);
      box-shadow: 0 1px 40px rgba(0,0,0,.8), 0 0 0 0 transparent;
    }
    .nav-brand {
      font-size:.72rem; text-transform:uppercase; letter-spacing:.28em;
      color: var(--gold);
    }
    .nav-cta {
      background: var(--blood);
      color: #fff !important;
      padding: 9px 26px;
      border: 1px solid var(--crimson);
      border-radius: 1px;
      font-size:.65rem;
      text-transform:uppercase;
      letter-spacing:.22em;
      transition: background .2s, box-shadow .2s;
    }
    .nav-cta:hover {
      background: var(--crimson);
      box-shadow: 0 0 24px rgba(163,21,21,.6);
    }

    /* ═══════════════════════════════════════════
       HERO
    ═══════════════════════════════════════════ */
    .hero {
      min-height: 100svh;
      display:flex; flex-direction:column;
      justify-content:center; align-items:center;
      text-align:center;
      padding: 100px 24px 80px;
      position:relative; overflow:hidden;
    }

    /* Deep red vortex behind hero text */
    .hero-glow {
      position:absolute;
      width:900px; height:900px;
      top:50%; left:50%;
      transform: translate(-50%,-50%);
      background: radial-gradient(ellipse,
        rgba(123,0,0,.28) 0%,
        rgba(123,0,0,.06) 40%,
        transparent 70%);
      pointer-events:none;
      animation: breathe 7s ease-in-out infinite;
    }
    @keyframes breathe {
      0%,100% { transform:translate(-50%,-50%) scale(1); opacity:.8; }
      50%      { transform:translate(-50%,-50%) scale(1.12); opacity:1; }
    }

    /* Animated ember sparks */
    .spark {
      position:absolute;
      border-radius:50%;
      background: var(--blood);
      pointer-events:none;
      animation: rise linear infinite;
    }
    @keyframes rise {
      0%   { transform:translateY(0) scale(.6); opacity:.9; }
      100% { transform:translateY(-100vh) scale(.2); opacity:0; }
    }

    .eyebrow {
      font-size:.62rem; text-transform:uppercase; letter-spacing:.38em;
      color: var(--fire);
      margin-bottom:28px;
      animation: fadein .9s ease both;
    }

    .hero h1 {
      font-size: clamp(3.2rem, 9vw, 7.5rem);
      color: #fff;
      text-shadow:
        0 0 80px rgba(123,0,0,.9),
        0 0 20px rgba(123,0,0,.5),
        0 3px 0 rgba(0,0,0,1);
      animation: fadein .9s .12s ease both;
      margin-bottom: 4px;
    }
    .hero h1 span { color: var(--fire); }

    .hero-sub {
      font-family: 'Cormorant SC', Georgia, serif;
      font-size: clamp(.78rem,1.8vw,.98rem);
      letter-spacing:.12em;
      color: var(--gold);
      max-width:620px;
      margin:.4rem auto 1rem;
      animation: fadein .9s .24s ease both;
    }
    .hero-by {
      font-style:italic;
      font-size:1.05rem;
      color: var(--ash);
      margin-bottom:2.4rem;
      animation: fadein .9s .34s ease both;
    }

    /* Ornamental rule */
    .ornament {
      display:flex; align-items:center; gap:14px;
      justify-content:center; margin:2rem auto;
      animation: fadein .9s .42s ease both;
    }
    .ornament::before, .ornament::after {
      content:'';
      width:90px; height:1px;
    }
    .ornament::before { background:linear-gradient(90deg,transparent,var(--blood)); }
    .ornament::after  { background:linear-gradient(90deg,var(--blood),transparent); }
    .ornament-sym { font-size:1.3rem; color:var(--blood); }

    .hero-hook {
      font-size: clamp(1.15rem,2.8vw,1.5rem);
      color: var(--parchment);
      max-width:680px;
      margin:0 auto 3rem;
      line-height:1.65;
      animation: fadein .9s .52s ease both;
    }

    @keyframes fadein {
      from { opacity:0; transform:translateY(22px); }
      to   { opacity:1; transform:translateY(0); }
    }

    /* ── Buttons ── */
    .btn-primary {
      display:inline-block;
      padding:17px 54px;
      background:linear-gradient(140deg, var(--blood) 0%, var(--crimson) 60%, var(--fire) 100%);
      color:#fff; border:none; border-radius:1px;
      font-size:.72rem; text-transform:uppercase; letter-spacing:.22em;
      cursor:pointer;
      box-shadow:
        0 0 40px rgba(123,0,0,.55),
        0 2px 0 rgba(255,255,255,.08) inset,
        0 -2px 0 rgba(0,0,0,.4) inset;
      transition: transform .2s, box-shadow .2s;
      animation: fadein .9s .64s ease both;
    }
    .btn-primary:hover {
      transform:translateY(-3px);
      box-shadow: 0 0 65px rgba(163,21,21,.75), 0 8px 20px rgba(0,0,0,.5);
      color:#fff;
    }

    .btn-outline {
      display:inline-block;
      padding:14px 42px;
      background:transparent;
      color: var(--gold);
      border:1px solid var(--gold);
      border-radius:1px;
      font-size:.7rem; text-transform:uppercase; letter-spacing:.2em;
      cursor:pointer;
      transition: background .2s, box-shadow .2s, color .2s;
    }
    .btn-outline:hover {
      background:rgba(201,168,76,.1);
      box-shadow:0 0 28px rgba(201,168,76,.28);
      color:var(--gold-hi);
    }

    /* ═══════════════════════════════════════════
       STATS RIBBON
    ═══════════════════════════════════════════ */
    .ribbon {
      background:
        linear-gradient(135deg, var(--obsidian) 0%, var(--slate) 100%);
      border-top:1px solid rgba(123,0,0,.35);
      border-bottom:1px solid rgba(123,0,0,.35);
      padding:32px 40px;
    }
    .ribbon-inner {
      max-width:860px; margin:0 auto;
      display:flex; flex-wrap:wrap;
      justify-content:center; gap:40px;
    }
    .stat { text-align:center; }
    .stat-num {
      font-family:'Trajan Pro 3','Cinzel Decorative',serif;
      font-size:2.4rem;
      color: var(--fire);
      display:block;
      text-shadow:0 0 20px rgba(214,48,49,.45);
    }
    .stat-label {
      font-size:.6rem; text-transform:uppercase; letter-spacing:.28em;
      color:var(--ash);
    }

    /* ═══════════════════════════════════════════
       GENERIC SECTION CHROME
    ═══════════════════════════════════════════ */
    .section { padding:96px 24px; }
    .container { max-width:840px; margin:0 auto; }

    .label-tag {
      font-size:.6rem; text-transform:uppercase; letter-spacing:.35em;
      color: var(--fire); margin-bottom:12px; display:block;
    }
    .section-h {
      font-size:clamp(1.8rem,4.5vw,2.9rem);
      color:#fff; margin-bottom:28px;
    }
    .section-h span { color:var(--fire); }

    .prose p { margin-bottom:1.15rem; font-size:1.02rem; line-height:1.85; }

    .pull {
      border-left:3px solid var(--blood);
      padding:18px 28px;
      margin:2.4rem 0;
      background:rgba(123,0,0,.07);
      border-radius:0 4px 4px 0;
    }
    .pull p {
      font-size:1.2rem; font-style:italic;
      color:var(--parchment); margin:0; line-height:1.6;
    }

    /* ═══════════════════════════════════════════
       TRADITION CARDS
    ═══════════════════════════════════════════ */
    .card-grid {
      display:grid;
      grid-template-columns: repeat(auto-fit, minmax(272px, 1fr));
      gap:20px; margin-top:44px;
    }
    .tcard {
      background:linear-gradient(150deg, var(--obsidian) 0%, rgba(30,0,0,.35) 100%);
      border:1px solid rgba(123,0,0,.22);
      border-radius:3px; padding:30px 26px;
      position:relative; overflow:hidden;
      transition:border-color .25s, box-shadow .25s, transform .25s;
    }
    .tcard::after {
      content:'';
      position:absolute; top:0; left:0; right:0; height:2px;
      background:linear-gradient(90deg,transparent,var(--blood),transparent);
      opacity:0; transition:opacity .25s;
    }
    .tcard:hover {
      border-color:rgba(163,21,21,.55);
      box-shadow:0 6px 40px rgba(123,0,0,.22);
      transform:translateY(-3px);
    }
    .tcard:hover::after { opacity:1; }

    .card-icon { font-size:2rem; display:block; margin-bottom:14px; opacity:.85; }
    .card-name {
      font-size:.8rem; text-transform:uppercase; letter-spacing:.14em;
      color:var(--gold); margin-bottom:10px;
    }
    .card-body { font-size:.93rem; color:var(--ash); line-height:1.68; }

    /* ═══════════════════════════════════════════
       THREE MODELS
    ═══════════════════════════════════════════ */
    .models-bg {
      background:linear-gradient(180deg,
        rgba(30,0,0,.18) 0%, transparent 40%, rgba(30,0,0,.12) 100%);
      border-top:1px solid rgba(123,0,0,.18);
      border-bottom:1px solid rgba(123,0,0,.18);
    }
    .model-list { list-style:none; margin-top:36px; display:flex; flex-direction:column; gap:16px; }
    .model-item {
      display:grid; grid-template-columns:64px 1fr;
      gap:20px; align-items:start;
      background:rgba(123,0,0,.07);
      border:1px solid rgba(123,0,0,.18);
      border-radius:3px; padding:22px 24px;
    }
    .model-roman {
      font-size:2rem; color:var(--blood);
      text-align:center; line-height:1;
      padding-top:4px;
    }
    .model-name {
      font-family:'Cormorant SC',serif;
      font-size:.85rem; letter-spacing:.12em;
      color:var(--parchment); margin-bottom:6px;
    }
    .model-desc { font-size:.93rem; color:var(--ash); line-height:1.65; }

    /* ═══════════════════════════════════════════
       MAIN CTA BLOCK
    ═══════════════════════════════════════════ */
    .cta-block {
      text-align:center;
      padding:110px 24px;
      position:relative; overflow:hidden;
    }
    .cta-block::before {
      content:'';
      position:absolute; inset:0; pointer-events:none;
      background:radial-gradient(ellipse 70% 60% at 50% 50%,
        rgba(123,0,0,.2) 0%, transparent 70%);
    }
    .price {
      font-family:'Trajan Pro 3','Cinzel Decorative',serif;
      font-size:4rem; color:var(--gold-hi);
      text-shadow:0 0 40px rgba(201,168,76,.45);
      display:block; margin:18px 0 6px;
    }
    .price-note { font-size:.8rem; color:var(--ash); letter-spacing:.06em; margin-bottom:34px; }
    .guarantee {
      display:inline-flex; align-items:center; gap:10px;
      margin-top:26px; font-size:.78rem; color:var(--ash);
      font-family:'Cormorant SC',serif; letter-spacing:.1em;
    }

    /* ═══════════════════════════════════════════
       UPSELL — SPIRITUAL GIANT SERIES
    ═══════════════════════════════════════════ */
    .upsell {
      background:linear-gradient(180deg,
        var(--jet) 0%, rgba(15,0,0,.3) 50%, var(--jet) 100%);
      border-top:1px solid rgba(123,0,0,.45);
      border-bottom:1px solid rgba(123,0,0,.45);
      padding:110px 24px;
    }
    .upsell-head { text-align:center; margin-bottom:64px; }
    .badge {
      display:inline-block;
      background:var(--blood); color:#fff;
      font-size:.6rem; text-transform:uppercase; letter-spacing:.28em;
      padding:6px 20px; border-radius:30px; margin-bottom:20px;
    }
    .upsell-title { font-size:clamp(1.9rem,5vw,3.2rem); color:#fff; margin-bottom:12px; }
    .upsell-tagline { font-style:italic; color:var(--gold); font-size:1.1rem; }

    .series-grid {
      display:grid;
      grid-template-columns:repeat(auto-fit,minmax(270px,1fr));
      gap:24px; max-width:1020px; margin:0 auto 56px;
    }
    .scard {
      background:linear-gradient(160deg, var(--obsidian) 0%, rgba(20,0,0,.55) 100%);
      border:1px solid rgba(123,0,0,.32);
      border-radius:4px; padding:32px 28px;
      position:relative; overflow:hidden;
      transition:transform .25s, box-shadow .25s;
    }
    .scard::after {
      content:'';
      position:absolute; bottom:0; left:0; right:0; height:3px;
      background:linear-gradient(90deg,var(--blood),var(--fire),var(--blood));
      opacity:0; transition:opacity .25s;
    }
    .scard:hover { transform:translateY(-5px); box-shadow:0 16px 50px rgba(123,0,0,.3); }
    .scard:hover::after { opacity:1; }

    .scard-num {
      font-family:'Cormorant SC',serif;
      font-size:.62rem; letter-spacing:.22em; text-transform:uppercase;
      color:var(--fire); margin-bottom:10px; display:block;
    }
    .scard-title {
      font-family:'Cormorant SC',serif;
      font-size:1.08rem; color:var(--parchment);
      margin-bottom:14px; line-height:1.35;
    }
    .scard-desc { font-size:.9rem; color:var(--ash); line-height:1.68; margin-bottom:20px; }
    .scard-link {
      font-family:'Cormorant SC',serif;
      font-size:.65rem; letter-spacing:.2em; text-transform:uppercase;
      color:var(--fire);
      border-bottom:1px solid rgba(214,48,49,.3); padding-bottom:2px;
      transition:color .2s, border-color .2s;
    }
    .scard-link:hover { color:var(--gold-hi); border-color:var(--gold-hi); }

    .bundle-box {
      max-width:620px; margin:0 auto; text-align:center;
      background:linear-gradient(140deg, rgba(123,0,0,.13) 0%, rgba(20,0,0,.6) 100%);
      border:1px solid rgba(123,0,0,.5); border-radius:6px;
      padding:50px 40px;
    }
    .bundle-box h3 {
      font-family:'Cormorant SC',serif;
      font-size:1.3rem; color:var(--gold); letter-spacing:.12em; margin-bottom:16px;
    }
    .bundle-box p { font-size:1rem; color:var(--silver); margin-bottom:30px; line-height:1.72; }

    /* ═══════════════════════════════════════════
       AUTHOR SECTION
    ═══════════════════════════════════════════ */
    .author-section {
      background:var(--obsidian);
      border-top:1px solid rgba(255,255,255,.045);
    }
    .author-wrap {
      max-width:840px; margin:0 auto;
      display:flex; gap:52px; align-items:flex-start; flex-wrap:wrap;
    }
    .author-seal {
      width:96px; height:96px; flex-shrink:0;
      border-radius:50%;
      background:linear-gradient(135deg,var(--blood),var(--void));
      border:2px solid var(--blood);
      display:flex; align-items:center; justify-content:center;
      font-family:'Trajan Pro 3','Cinzel Decorative',serif;
      font-size:1.8rem; color:var(--gold);
    }
    .author-body { flex:1; min-width:260px; }
    .author-body h4 { color:var(--parchment); margin-bottom:6px; letter-spacing:.06em; }
    .author-links { display:flex; flex-wrap:wrap; gap:12px; margin-top:20px; }
    .author-links a {
      font-family:'Cormorant SC',serif;
      font-size:.65rem; letter-spacing:.18em; text-transform:uppercase;
      color:var(--fire); padding:6px 16px;
      border:1px solid rgba(214,48,49,.3);
      border-radius:1px; transition:all .2s;
    }
    .author-links a:hover {
      background:rgba(214,48,49,.1);
      border-color:var(--fire); color:var(--fire);
    }

    /* ═══════════════════════════════════════════
       FOOTER
    ═══════════════════════════════════════════ */
    footer {
      background:var(--gloss);
      border-top:1px solid rgba(123,0,0,.25);
      padding:42px 40px; text-align:center;
    }
    footer .wordmark {
      font-family:'Trajan Pro 3','Cinzel Decorative',serif;
      font-size:.95rem; color:var(--blood);
      display:block; margin-bottom:10px;
    }
    footer p {
      font-family:'Cormorant SC',serif;
      font-size:.62rem; letter-spacing:.2em;
      color:rgba(112,112,112,.55); text-transform:uppercase;
    }

    /* ═══════════════════════════════════════════
       SCROLL REVEAL
    ═══════════════════════════════════════════ */
    .reveal {
      opacity:0; transform:translateY(32px);
      transition: opacity .72s ease, transform .72s ease;
    }
    .reveal.in { opacity:1; transform:translateY(0); }

    /* ═══════════════════════════════════════════
       RESPONSIVE
    ═══════════════════════════════════════════ */
    @media(max-width:600px) {
      nav { padding:14px 20px; }
      .hero h1 { font-size:2.6rem; }
      .author-wrap { flex-direction:column; }
      .price { font-size:2.8rem; }
      .bundle-box { padding:36px 22px; }
    }
    """)


def js() -> str:
    """Return the page JavaScript — scroll reveal + ember particle system."""
    return dedent("""
    // ── Scroll-reveal observer ──────────────────────────
    const io = new IntersectionObserver((entries) => {
      entries.forEach((entry, idx) => {
        if (entry.isIntersecting) {
          // Stagger siblings in the same parent grid/list
          const siblings = entry.target.parentElement
            .querySelectorAll('.reveal');
          siblings.forEach((el, i) => {
            el.style.transitionDelay = (i * 0.07) + 's';
          });
          entry.target.classList.add('in');
        }
      });
    }, { threshold: 0.10 });

    document.querySelectorAll('.reveal').forEach(el => io.observe(el));

    // ── Ember particle spawner ──────────────────────────
    (function spawnEmbers() {
      const colors = ['#7B0000','#A31515','#D63031','#C9A84C'];
      const hero   = document.querySelector('.hero');
      if (!hero) return;

      function spawn() {
        const el = document.createElement('div');
        el.className = 'spark';
        const size = Math.random() * 5 + 2;
        const dur  = Math.random() * 8 + 6;
        el.style.cssText = [
          `width:${size}px`, `height:${size}px`,
          `left:${Math.random()*100}%`,
          `bottom:0`,
          `background:${colors[Math.floor(Math.random()*colors.length)]}`,
          `animation-duration:${dur}s`,
          `animation-delay:${Math.random()*4}s`,
          `box-shadow:0 0 ${size*2}px ${colors[0]}`
        ].join(';');
        hero.appendChild(el);
        setTimeout(() => el.remove(), (dur + 4) * 1000);
      }

      // Initial burst
      for (let i = 0; i < 14; i++) setTimeout(spawn, i * 400);
      // Continuous trickle
      setInterval(spawn, 900);
    })();
    """)


def nav_html() -> str:
    return f"""
<nav class="layer">
  <span class="nav-brand">FaithfulBooks Publishing</span>
  <a href="{BOOK['gumroad_url']}" class="nav-cta" target="_blank">
    Get the Book
  </a>
</nav>"""


def hero_html() -> str:
    return f"""
<header class="hero layer">
  <div class="hero-glow"></div>

  <span class="eyebrow">A Landmark Work of Comparative Spiritual History</span>

  <h1>
    Gods of<br/>
    <span>the Nations</span>
  </h1>

  <p class="hero-sub">
    {BOOK['subtitle']}
  </p>

  <p class="hero-by">by {BOOK['author']}</p>

  <div class="ornament">
    <span class="ornament-sym">✦</span>
  </div>

  <p class="hero-hook">
    From the fire temples of ancient Persia to the Norse death-drums of
    <em>Ragnarök</em> — from the <em>gallu</em> demons of Sumer to the Archons of
    Gnostic cosmology — every civilization that has ever existed arrived at the
    same terrifying conclusion:
    <br/><br/>
    <strong>Something unseen opposes you.</strong>
  </p>

  <a href="{BOOK['gumroad_url']}" class="btn-primary" target="_blank">
    Claim Your Copy
  </a>
</header>"""


def ribbon_html() -> str:
    stats = [
        (str(BOOK['pages']), "Pages of Research"),
        ("4,000+",           "Years of History"),
        ("12+",              "Ancient Civilizations"),
        ("3",                "Cosmological Models"),
    ]
    items = "\n".join(
        f'<div class="stat">'
        f'<span class="stat-num">{n}</span>'
        f'<span class="stat-label">{l}</span>'
        f'</div>'
        for n, l in stats
    )
    return f"""
<div class="ribbon layer">
  <div class="ribbon-inner">{items}</div>
</div>"""


def question_section_html() -> str:
    return f"""
<section class="section layer">
  <div class="container">
    <span class="label-tag reveal">The Central Question</span>
    <h2 class="section-h reveal">
      Why Did <span>Every Civilization</span><br/>Invent the Same Enemy?
    </h2>

    <div class="prose reveal">
      <p>Sumerian priests in 2500&nbsp;BCE described demons called the <em>gallu</em>
      dragging souls into the underworld. Egyptian scribes carved the name of Apep —
      the serpent of absolute chaos who attacks the solar barque of Ra every single night.
      Iranian prophets declared that Angra Mainyu, the Destructive Spirit, wages cosmic war
      against all creation. Norse skalds recorded the world-serpent Jörmungandr, who will
      swallow reality at Ragnarök. Indian philosophers mapped the <em>Asuras</em>.
      Gnostic teachers named the Archons — cosmic prison wardens who trap human souls in matter.</p>

      <p>These civilizations shared no scripture, no common ancestor tradition, no contact.
      They arose on different continents, in different millennia, speaking utterly different
      languages. Yet all of them, independently, mapped an identical enemy.</p>
    </div>

    <div class="pull reveal">
      <p>"The specific names differ. The cosmological architectures differ.
      The proposed remedies differ enormously. But the underlying intuition —
      that something unseen opposes human flourishing — remains remarkably stable
      across the full breadth of human culture."</p>
    </div>

    <div class="prose reveal">
      <p><strong>That consistency demands explanation.</strong> Not dismissal. Not
      reduction to primitive superstition. Serious forensic inquiry. And that is precisely
      what Adam Joseph Hanrahan delivers in this landmark 198-page work.</p>
      <p><em>Gods of the Nations</em> is not another entry in the spiritual warfare genre
      that simply re-reads familiar Bible verses. It sets the familiar framework aside
      entirely to interrogate the cross-cultural record — the kind of book that
      permanently changes how you see every headline, every cultural collapse,
      every moment of spiritual oppression you have ever experienced.</p>
    </div>
  </div>
</section>"""


def traditions_section_html() -> str:
    cards = "\n".join(
        f"""<div class="tcard reveal">
  <span class="card-icon">{t['icon']}</span>
  <div class="card-name">{t['name']}</div>
  <p class="card-body">{t['body']}</p>
</div>"""
        for t in TRADITIONS
    )
    return f"""
<section class="section layer">
  <div class="container">
    <span class="label-tag reveal">Inside the Book</span>
    <h2 class="section-h reveal">
      Six Civilizations.<br/><span>One Terrifying Pattern.</span>
    </h2>
    <div class="card-grid">{cards}</div>
  </div>
</section>"""


def models_section_html() -> str:
    items = "\n".join(
        f"""<li class="model-item reveal">
  <div class="model-roman">{m['roman']}</div>
  <div>
    <div class="model-name">{m['name']}</div>
    <p class="model-desc">{m['desc']}</p>
  </div>
</li>"""
        for m in MODELS
    )
    return f"""
<section class="section models-bg layer">
  <div class="container">
    <span class="label-tag reveal">The Book's Structural Discovery</span>
    <h2 class="section-h reveal">
      Three Models of<br/><span>Cosmic Opposition</span>
    </h2>

    <div class="prose reveal">
      <p>Beneath the surface diversity of names, rituals, and mythological narratives,
      Hanrahan identifies three fundamental cosmological models that every adversarial
      tradition resolves into — and shows how each illuminates a different dimension
      of spiritual reality that the others leave in shadow.</p>
    </div>

    <ul class="model-list">{items}</ul>

    <div class="pull reveal" style="margin-top:2.4rem">
      <p>"The evolution of evil is not a story of humanity outgrowing its fear of darkness.
      It is a story of humanity's progressive deepening of its engagement with one of the
      most fundamental features of conscious existence."</p>
    </div>

    <div class="prose reveal" style="margin-top:1.6rem">
      <p><strong>This is not theoretical.</strong> Every chapter maps directly onto
      observable spiritual, cultural, and psychological dynamics happening right now.
      You will leave this book with a complete cross-cultural framework for recognizing
      adversarial patterns — and responding with the full accumulated intelligence of
      the human spiritual tradition.</p>
    </div>
  </div>
</section>"""


def cta_block_html() -> str:
    return f"""
<section class="cta-block layer" id="buy">
  <div class="container">
    <span class="label-tag reveal">Get the Book</span>
    <h2 class="section-h reveal">
      Ready to See<br/><span>What Every Civilization Saw?</span>
    </h2>

    <div class="prose reveal" style="text-align:center;max-width:560px;margin:0 auto">
      <p>Stop fighting an enemy you cannot name. <em>Gods of the Nations</em> gives you
      the full cross-cultural map — 4,000 years of accumulated human intelligence about
      what opposes you, how it operates, and how spiritual warriors in every tradition
      have responded.</p>
    </div>

    <span class="price reveal">$9.99</span>
    <p class="price-note reveal">
      Gumroad &nbsp;·&nbsp; Amazon Kindle &nbsp;·&nbsp; Google Play Books
    </p>

    <a href="{BOOK['gumroad_url']}" class="btn-primary reveal" target="_blank"
       style="animation:none">
      Get Gods of the Nations &rarr;
    </a>

    <div class="guarantee reveal">
      <span>✦</span>
      <span>Published by FaithfulBooks &nbsp;·&nbsp;
      "Where survival isn't the victory — staying human is."</span>
    </div>
  </div>
</section>"""


def upsell_html() -> str:
    series_cards = "\n".join(
        f"""<div class="scard reveal">
  <span class="scard-num">{s['num']}</span>
  <div class="scard-title">{s['title']}</div>
  <p class="scard-desc">{s['desc']}</p>
  <a href="{s['url']}" class="scard-link" target="_blank">{s['cta']}</a>
</div>"""
        for s in SERIES
    )

    return f"""
<section class="upsell layer" id="series">
  <div class="upsell-head reveal">
    <span class="badge">Complete Your Training</span>
    <h2 class="upsell-title">
      The Spiritual Giant Series
    </h2>
    <p class="upsell-tagline">
      "You've seen the map. Now learn to fight."
    </p>
  </div>

  <div class="series-grid">{series_cards}</div>

  <div class="bundle-box reveal">
    <h3>⚔ The Complete Spiritual Giant Bundle</h3>
    <p>
      Combine <em>Gods of the Nations</em> with the full Soul Cage Trilogy —
      the complete intelligence package for anyone ready to stop being a victim
      in this war and start operating as a trained spiritual warrior.
      Available as an exclusive bundle on Gumroad.
    </p>
    <a href="{BOOK['gumroad_url']}" class="btn-outline" target="_blank">
      View the Bundle on Gumroad &rarr;
    </a>
  </div>
</section>"""


def author_html() -> str:
    return f"""
<section class="section author-section layer">
  <div class="author-wrap">
    <div class="author-seal">AH</div>
    <div class="author-body">
      <span class="label-tag">About the Author</span>
      <h4>{BOOK['author']}</h4>
      <div class="prose">
        <p>
          Adam Joseph Hanrahan is a bold voice at the intersection of ancient wisdom,
          spiritual warfare, modern conspiracy, and cutting-edge technology.
          Drawing from personal experience with America's criminal justice system,
          deep research into governmental operations, and profound spiritual inquiry,
          Hanrahan writes with unflinching honesty and meticulous sourcing.
          Through FaithfulBooks Publishing, his body of work spans supernatural thrillers,
          hard-hitting non-fiction exposés, and AI strategy guides — each one
          challenging readers to see past the surface of the world they think they know.
        </p>
      </div>
      <div class="author-links">
        <a href="{BOOK['gumroad_url']}"  target="_blank">Gumroad Store</a>
        <a href="{BOOK['kofi_url']}"     target="_blank">Ko-fi Support</a>
        <a href="{BOOK['google_play']}"  target="_blank">Google Play</a>
        <a href="{BOOK['site_url']}"     target="_blank">Publisher Site</a>
      </div>
    </div>
  </div>
</section>"""


def footer_html() -> str:
    return f"""
<footer class="layer">
  <span class="wordmark">FaithfulBooks</span>
  <p>&copy; 2026 {BOOK['author']} &nbsp;&middot;&nbsp; {BOOK['publisher']}
  &nbsp;&middot;&nbsp; West Warwick, RI</p>
  <p style="margin-top:6px">{BOOK['email']}</p>
</footer>"""


# ──────────────────────────────────────────────
#  ASSEMBLE THE FULL PAGE
# ──────────────────────────────────────────────

def build_page() -> str:
    """
    Concatenate every section into a single self-contained HTML document.
    The page uses:
      - Google Fonts (Cormorant Garamond + Cormorant SC for display elegance)
      - Pure CSS design tokens with no external framework dependency
      - Inline JS (no libraries — zero network risk for buyers)
    """
    google_fonts = (
        "https://fonts.googleapis.com/css2?"
        "family=Cormorant+Garamond:ital,wght@0,400;0,600;1,400;1,600&"
        "family=Cormorant+SC:wght@400;600;700&"
        "display=swap"
    )

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8"/>
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <meta name="description" content="{BOOK['subtitle']} — by {BOOK['author']}"/>
  <title>Gods of the Nations — {BOOK['author']}</title>
  <link rel="preconnect" href="https://fonts.googleapis.com"/>
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin/>
  <link href="{google_fonts}" rel="stylesheet"/>
  <style>{css()}</style>
</head>
<body>

{nav_html()}
{hero_html()}
{ribbon_html()}
{question_section_html()}
{traditions_section_html()}
{models_section_html()}
{cta_block_html()}
{upsell_html()}
{author_html()}
{footer_html()}

<script>{js()}</script>
</body>
</html>"""


# ──────────────────────────────────────────────
#  ENTRY POINT
# ──────────────────────────────────────────────

if __name__ == "__main__":
    output_path = Path("gods_of_nations_sales_page.html")
    html = build_page()
    output_path.write_text(html, encoding="utf-8")

    print(f"✅  Sales page written → {output_path.resolve()}")
    print(f"    File size : {output_path.stat().st_size / 1024:.1f} KB")
    print()
    print("── Gumroad deployment steps ──────────────────────────")
    print("  1. Open the .html file in your browser to preview it.")
    print("  2. Host it free on Netlify Drop: netlify.com/drop")
    print("     (drag the file into the browser — gets a live URL instantly)")
    print("  3. Or push to GitHub Pages / your own domain.")
    print("  4. In Gumroad → Edit Product → paste the hosted URL")
    print("     into 'Custom redirect URL' or embed it in the description.")
    print("  5. Buyers see the full sales experience before checkout.")
