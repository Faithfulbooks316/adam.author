/**
 * Adam Joseph Hanrahan — Author Landing Page
 * app.js — Interactions, animations, particle system
 * FaithfulBooks Publishing
 */

'use strict';

/* ── DOM REFS ─────────────────────────────────────── */
const nav         = document.getElementById('nav');
const navToggle   = document.getElementById('navToggle');
const navLinks    = document.getElementById('navLinks');
const cursor      = document.getElementById('cursor');
const cursorTrail = document.getElementById('cursorTrail');
const backTop     = document.getElementById('backTop');
const booksGrid   = document.getElementById('booksGrid');
const filterTabs  = document.querySelectorAll('.filter-tab');
const canvas      = document.getElementById('particleCanvas');
const ctx         = canvas ? canvas.getContext('2d') : null;


/* ══════════════════════════════════════════════════
   1. CUSTOM CURSOR
══════════════════════════════════════════════════ */
(function initCursor() {
  if (window.matchMedia('(pointer: coarse)').matches) return; // skip touch

  let mx = 0, my = 0;
  let tx = 0, ty = 0;

  document.addEventListener('mousemove', e => {
    mx = e.clientX;
    my = e.clientY;
    if (cursor) {
      cursor.style.left = mx + 'px';
      cursor.style.top  = my + 'px';
    }
  });

  // Trail lags behind
  function animateTrail() {
    tx += (mx - tx) * 0.12;
    ty += (my - ty) * 0.12;
    if (cursorTrail) {
      cursorTrail.style.left = tx + 'px';
      cursorTrail.style.top  = ty + 'px';
    }
    requestAnimationFrame(animateTrail);
  }
  animateTrail();

  // Scale cursor on interactive elements
  document.addEventListener('mouseover', e => {
    if (e.target.matches('a, button, [role="tab"]')) {
      if (cursor) {
        cursor.style.width  = '20px';
        cursor.style.height = '20px';
        cursor.style.background = '#E74C3C';
      }
    }
  });
  document.addEventListener('mouseout', e => {
    if (e.target.matches('a, button, [role="tab"]')) {
      if (cursor) {
        cursor.style.width  = '10px';
        cursor.style.height = '10px';
        cursor.style.background = '#D4AF37';
      }
    }
  });
})();


/* ══════════════════════════════════════════════════
   2. NAVIGATION — scroll state + mobile toggle
══════════════════════════════════════════════════ */
(function initNav() {
  let lastScroll = 0;

  window.addEventListener('scroll', () => {
    const y = window.scrollY;

    // Solid background after 80px
    nav.classList.toggle('scrolled', y > 80);

    // Back to top visibility
    backTop.classList.toggle('show', y > 500);

    lastScroll = y;
  }, { passive: true });

  // Mobile toggle
  navToggle.addEventListener('click', () => {
    const open = navToggle.classList.toggle('open');
    navLinks.classList.toggle('open', open);
    navToggle.setAttribute('aria-expanded', open);
  });

  // Close mobile menu on link click
  navLinks.querySelectorAll('a').forEach(link => {
    link.addEventListener('click', () => {
      navToggle.classList.remove('open');
      navLinks.classList.remove('open');
    });
  });

  // Back to top
  backTop.addEventListener('click', () => {
    window.scrollTo({ top: 0, behavior: 'smooth' });
  });

  // Active nav link on scroll (highlight current section)
  const sections = document.querySelectorAll('section[id]');
  const navAnchors = document.querySelectorAll('.nav-links a[href^="#"]');

  function updateActiveLink() {
    const scrollY = window.scrollY + 120;
    sections.forEach(section => {
      const top    = section.offsetTop;
      const height = section.offsetHeight;
      const id     = section.getAttribute('id');
      if (scrollY >= top && scrollY < top + height) {
        navAnchors.forEach(a => a.classList.remove('active'));
        const active = document.querySelector(`.nav-links a[href="#${id}"]`);
        if (active) active.classList.add('active');
      }
    });
  }
  window.addEventListener('scroll', updateActiveLink, { passive: true });
})();


/* ══════════════════════════════════════════════════
   3. BOOK FILTER TABS
══════════════════════════════════════════════════ */
(function initBookFilter() {
  const cards = document.querySelectorAll('.book-card');

  filterTabs.forEach(tab => {
    tab.addEventListener('click', () => {
      // Update active tab
      filterTabs.forEach(t => t.classList.remove('active'));
      tab.classList.add('active');

      const filter = tab.dataset.filter;

      // Animate cards
      cards.forEach((card, i) => {
        const cat = card.dataset.category;
        const show = filter === 'all' || cat === filter;

        if (show) {
          card.classList.remove('hidden');
          // Stagger re-entry
          setTimeout(() => {
            card.style.transitionDelay = (i * 0.04) + 's';
            card.classList.add('visible');
          }, 10);
        } else {
          card.classList.remove('visible');
          card.style.transitionDelay = '0s';
          // Delay hiding to allow fade out
          setTimeout(() => card.classList.add('hidden'), 350);
        }
      });
    });
  });
})();


/* ══════════════════════════════════════════════════
   4. INTERSECTION OBSERVER — scroll reveal
══════════════════════════════════════════════════ */
(function initScrollReveal() {
  // Reveal [data-aos] elements
  const aosObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        // Stagger siblings in same parent
        const parent   = entry.target.parentElement;
        const siblings = parent.querySelectorAll('[data-aos]');
        siblings.forEach((el, i) => {
          el.style.transitionDelay = (i * 0.08) + 's';
        });
        entry.target.classList.add('aos-in');
        aosObserver.unobserve(entry.target);
      }
    });
  }, { threshold: 0.1, rootMargin: '0px 0px -40px 0px' });

  document.querySelectorAll('[data-aos]').forEach(el => aosObserver.observe(el));

  // Reveal book cards
  const cardObserver = new IntersectionObserver((entries) => {
    entries.forEach((entry, idx) => {
      if (entry.isIntersecting && !entry.target.classList.contains('hidden')) {
        entry.target.classList.add('visible');
        cardObserver.unobserve(entry.target);
      }
    });
  }, { threshold: 0.08, rootMargin: '0px 0px -30px 0px' });

  document.querySelectorAll('.book-card').forEach(card => cardObserver.observe(card));

  // Reveal general sections
  const sectionObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.style.opacity = '1';
        entry.target.style.transform = 'translateY(0)';
      }
    });
  }, { threshold: 0.06 });

  document.querySelectorAll(
    '.about-grid, .trilogy-book, .service-card, .platform-card, .contact-card'
  ).forEach(el => {
    el.style.opacity = '0';
    el.style.transform = 'translateY(20px)';
    el.style.transition = 'opacity .65s ease, transform .65s ease';
    sectionObserver.observe(el);
  });

  // Stagger trilogy books
  document.querySelectorAll('.trilogy-book').forEach((el, i) => {
    el.style.transitionDelay = (i * 0.15) + 's';
  });

  // Stagger service cards
  document.querySelectorAll('.service-card').forEach((el, i) => {
    el.style.transitionDelay = (i * 0.1) + 's';
  });

  // Stagger platform cards
  document.querySelectorAll('.platform-card').forEach((el, i) => {
    el.style.transitionDelay = (i * 0.06) + 's';
  });
})();


/* ══════════════════════════════════════════════════
   5. HERO PARTICLE SYSTEM
   Red ember sparks + floating gold specks
══════════════════════════════════════════════════ */
(function initParticles() {
  if (!canvas || !ctx) return;

  let W, H;
  const particles = [];

  function resize() {
    W = canvas.width  = canvas.offsetWidth;
    H = canvas.height = canvas.offsetHeight;
  }
  resize();
  window.addEventListener('resize', resize);

  const COLORS = [
    'rgba(107,0,0,',      // blood
    'rgba(153,0,0,',      // crimson
    'rgba(192,57,43,',    // fire
    'rgba(184,148,31,',   // gold
    'rgba(212,175,55,',   // gold hi
  ];

  class Particle {
    constructor() { this.reset(true); }

    reset(initial = false) {
      this.x    = Math.random() * W;
      this.y    = initial ? Math.random() * H : H + 10;
      this.size = Math.random() * 2.5 + .5;
      this.speed = Math.random() * .6 + .2;
      this.vx   = (Math.random() - .5) * .4;
      this.vy   = -(Math.random() * .8 + .3);
      this.life = 0;
      this.maxLife = Math.random() * 200 + 120;
      this.color = COLORS[Math.floor(Math.random() * COLORS.length)];
    }

    update() {
      this.x   += this.vx;
      this.y   += this.vy;
      this.life++;
      // Flicker drift
      this.vx  += (Math.random() - .5) * .04;
      if (this.life > this.maxLife || this.y < -10) this.reset();
    }

    draw() {
      const alpha = Math.sin((this.life / this.maxLife) * Math.PI) * .7;
      ctx.beginPath();
      ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
      ctx.fillStyle = this.color + alpha + ')';
      // Glow
      ctx.shadowBlur = this.size * 4;
      ctx.shadowColor = this.color + '.6)';
      ctx.fill();
      ctx.shadowBlur = 0;
    }
  }

  // Initialise pool
  for (let i = 0; i < 90; i++) particles.push(new Particle());

  function animate() {
    ctx.clearRect(0, 0, W, H);
    particles.forEach(p => { p.update(); p.draw(); });
    requestAnimationFrame(animate);
  }
  animate();
})();


/* ══════════════════════════════════════════════════
   6. SMOOTH ANCHOR SCROLL
══════════════════════════════════════════════════ */
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
  anchor.addEventListener('click', e => {
    const target = document.querySelector(anchor.getAttribute('href'));
    if (!target) return;
    e.preventDefault();
    const offset = 80; // nav height
    const top = target.getBoundingClientRect().top + window.scrollY - offset;
    window.scrollTo({ top, behavior: 'smooth' });
  });
});


/* ══════════════════════════════════════════════════
   7. PARALLAX — hero content subtle movement
══════════════════════════════════════════════════ */
(function initParallax() {
  const heroContent = document.querySelector('.hero-content');
  const heroGrid    = document.querySelector('.hero-grid');
  if (!heroContent || !heroGrid) return;

  let ticking = false;
  window.addEventListener('scroll', () => {
    if (!ticking) {
      requestAnimationFrame(() => {
        const y = window.scrollY;
        heroContent.style.transform = `translateY(${y * 0.25}px)`;
        heroGrid.style.transform    = `translateY(${y * 0.12}px)`;
        ticking = false;
      });
      ticking = true;
    }
  }, { passive: true });
})();


/* ══════════════════════════════════════════════════
   8. TYPEWRITER — hero tagline cycling
══════════════════════════════════════════════════ */
(function initTypewriter() {
  const tagline = document.querySelector('.hero-tagline');
  if (!tagline) return;

  const phrases = [
    'Author  ·  Truth Seeker  ·  Storyteller of the Hidden Realms',
    'Exposing Government Lies Since Day One',
    'Mapping Mankind\'s Oldest War',
    'Where Survival Isn\'t the Victory — Staying Human Is',
  ];

  let phraseIdx = 0;
  let charIdx   = 0;
  let deleting  = false;
  let paused    = false;
  const SPEED_TYPE = 42;
  const SPEED_DEL  = 22;
  const PAUSE_MS   = 2800;

  function tick() {
    const phrase = phrases[phraseIdx];

    if (!deleting) {
      charIdx++;
      tagline.textContent = phrase.slice(0, charIdx);
      if (charIdx === phrase.length) {
        paused = true;
        setTimeout(() => { paused = false; deleting = true; }, PAUSE_MS);
      }
    } else {
      charIdx--;
      tagline.textContent = phrase.slice(0, charIdx);
      if (charIdx === 0) {
        deleting = false;
        phraseIdx = (phraseIdx + 1) % phrases.length;
      }
    }

    if (!paused) setTimeout(tick, deleting ? SPEED_DEL : SPEED_TYPE);
  }

  // Start after hero animations finish
  setTimeout(tick, 1400);
})();


/* ══════════════════════════════════════════════════
   9. BOOK CARD TILT (mouse-over micro-interaction)
══════════════════════════════════════════════════ */
(function initCardTilt() {
  if (window.matchMedia('(pointer: coarse)').matches) return;

  document.querySelectorAll('.book-card-inner').forEach(card => {
    card.addEventListener('mousemove', e => {
      const rect = card.getBoundingClientRect();
      const x = (e.clientX - rect.left) / rect.width  - .5;
      const y = (e.clientY - rect.top)  / rect.height - .5;
      card.style.transform =
        `translateY(-6px) rotateY(${x * 8}deg) rotateX(${-y * 6}deg)`;
    });
    card.addEventListener('mouseleave', () => {
      card.style.transform = '';
    });
  });
})();


/* ══════════════════════════════════════════════════
   10. INIT — trigger initial state
══════════════════════════════════════════════════ */
document.addEventListener('DOMContentLoaded', () => {
  // Show all book cards by default
  document.querySelectorAll('.book-card').forEach((card, i) => {
    setTimeout(() => card.classList.add('visible'), i * 60);
  });

  // Add AOS attributes to section elements that need it
  const aosTargets = [
    '.about-grid',
    '.bundle-inner',
    '.gumroad-cta-card',
    '.contact-alt',
  ];
  aosTargets.forEach(sel => {
    document.querySelectorAll(sel).forEach(el => {
      if (!el.hasAttribute('data-aos')) el.setAttribute('data-aos', '');
    });
  });

  console.log(
    '%c✦ FaithfulBooks Publishing %c\nAdam Joseph Hanrahan\nWhere survival isn\'t the victory — staying human is.',
    'color:#D4AF37;font-family:serif;font-size:14px;font-weight:bold;',
    'color:#C0392B;font-family:serif;font-size:12px;'
  );
});
