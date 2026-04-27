/* ════════════════════════════════════════════════════════════════
   Talks Design System — canonical engine
   Source of truth. Do not edit per-deck copies.
   Responsibilities:
     1. Scale the 1280×720 deck to viewport
     2. Keyboard / touch / click navigation
     3. Progress bar + slide counter
     4. Auto-inject .brand-footer into content slides
   ════════════════════════════════════════════════════════════════ */
(function() {
  const deck = document.querySelector('.deck');
  if (!deck) return;
  const BASE_W = 1280, BASE_H = 720;

  /* ── 1. Scale ── */
  function scaleDeck() {
    const vw = window.innerWidth, vh = window.innerHeight;
    const scale = Math.min(vw / BASE_W, vh / BASE_H);
    deck.style.transform = 'translate(-50%, -50%) scale(' + scale + ')';
  }
  window.addEventListener('resize', scaleDeck);
  scaleDeck();

  /* ── 4. Brand-footer auto-inject ──
     Skips slides already carrying .brand-footer, title-slide (logo
     already present), and any slide tagged .no-footer. Logo path
     resolves from a data-brand-logo attribute on <body>, or defaults
     to ../reference/kor-eng2.png (convention: decks live one folder
     below reference/). Opt-out per-deck via <body data-brand-footer="off">.
  */
  const brandOff = document.body.dataset.brandFooter === 'off';
  const logoPath = document.body.dataset.brandLogo || '../reference/kor-eng2.png';
  const brandText = document.body.dataset.brandText || 'Yonsei University';
  if (!brandOff) {
    document.querySelectorAll('.slide').forEach(s => {
      if (s.classList.contains('title-slide')) return;
      if (s.classList.contains('no-footer')) return;
      if (s.querySelector(':scope > .brand-footer')) return;
      const f = document.createElement('div');
      f.className = 'brand-footer';
      f.innerHTML = '<img src="' + logoPath + '" alt=""><span>' + brandText + '</span>';
      s.appendChild(f);
    });
  }

  /* ── 2 & 3. Navigation + indicators ── */
  const slides = document.querySelectorAll('.slide');
  const total = slides.length;
  let current = 0;
  for (let i = 0; i < total; i++) {
    if (slides[i].classList.contains('active')) { current = i; break; }
  }
  /* Move slide-num out of the transformed .deck so it stays at the
     true viewport bottom-right (and never gets clipped by slide overflow). */
  let slideNum = document.getElementById('slideNum');
  if (slideNum && slideNum.parentNode !== document.body) {
    document.body.appendChild(slideNum);
  }
  const progressBar = document.getElementById('progressBar');

  function updateIndicators() {
    if (slideNum) slideNum.textContent = (current + 1) + ' / ' + total;
    if (progressBar) progressBar.style.width = ((current + 1) / total * 100) + '%';
  }
  function show(n) {
    slides[current].classList.remove('active');
    current = Math.max(0, Math.min(total - 1, n));
    slides[current].classList.add('active');
    updateIndicators();
  }
  updateIndicators();

  document.addEventListener('keydown', function(e) {
    if (e.key === 'ArrowRight' || e.key === 'ArrowDown' || e.key === ' ' || e.key === 'PageDown') {
      e.preventDefault(); show(current + 1);
    } else if (e.key === 'ArrowLeft' || e.key === 'ArrowUp' || e.key === 'PageUp') {
      e.preventDefault(); show(current - 1);
    } else if (e.key === 'Home') {
      e.preventDefault(); show(0);
    } else if (e.key === 'End') {
      e.preventDefault(); show(total - 1);
    }
  });

  let touchStartX = 0;
  document.addEventListener('touchstart', function(e) { touchStartX = e.touches[0].clientX; });
  document.addEventListener('touchend', function(e) {
    const dx = e.changedTouches[0].clientX - touchStartX;
    if (Math.abs(dx) > 50) { dx < 0 ? show(current + 1) : show(current - 1); }
  });

  document.addEventListener('click', function(e) {
    if (e.target.tagName === 'A' || e.target.tagName === 'BUTTON') return;
    e.clientX > window.innerWidth / 2 ? show(current + 1) : show(current - 1);
  });
})();
