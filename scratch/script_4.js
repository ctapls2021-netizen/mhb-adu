
  function scaleDesign() {
    var container = document.getElementById('container');
    var clipper   = document.getElementById('clipper');
    if (!container || !clipper) return;

    if (window.innerWidth >= 1024) {
      /* ── Desktop: zoom sobre canvas 1920px (sin cambios) ── */
      var scale = window.innerWidth / 1920;
      container.style.transform       = 'none';
      container.style.transformOrigin = '';
      container.style.width           = '1920px';
      container.style.zoom            = scale;
      var h = Math.ceil(container.offsetHeight * scale);
      clipper.style.height       = h + 'px';
      document.body.style.height = h + 'px';
    } else {
      /* ── Mobile: canvas 480px escalado al viewport ── */
      var scale = window.innerWidth / 480;
      container.style.zoom            = '1';
      container.style.width           = '480px';
      container.style.transform       = 'scale(' + scale + ')';
      container.style.transformOrigin = 'top left';
      var h = Math.ceil(container.offsetHeight * scale);
      clipper.style.height       = h + 'px';
      document.body.style.height = h + 'px';
    }
  }

  window.addEventListener('resize', scaleDesign);
  if (document.readyState === 'loading') {
    window.addEventListener('DOMContentLoaded', scaleDesign);
  } else {
    scaleDesign();
  }
  window.addEventListener('load', scaleDesign);

  // ResizeObserver to dynamically update scroll height when images/fonts load or content changes
  (function() {
    var container = document.getElementById('container');
    if (container && typeof ResizeObserver !== 'undefined') {
      var ro = new ResizeObserver(function() {
        scaleDesign();
      });
      ro.observe(container);
    }
  })();

  // Universal click handler to scroll to lead form on any CTA button
  document.addEventListener('click', function(e) {
    var cta = e.target.closest('a[href="#estimate"], a[href="#lead-form"], [data-cta="form"], .header-desktop-btn, .css-h7jh0h, .css-orhuyv, .css-bo4u3g, .css-tsm8h9');

    if (cta) {
      if (cta.getAttribute && cta.getAttribute('href') && cta.getAttribute('href').startsWith('tel:')) return;
      if (cta.tagName === 'BUTTON' && cta.type === 'submit') return;

      e.preventDefault();
      e.stopPropagation();

      var isMobile = window.innerWidth < 1024;
      var formEl = isMobile ? document.getElementById('lead-form') : document.getElementById('estimate');
      if (!formEl) formEl = document.getElementById('estimate') || document.getElementById('lead-form');

      if (formEl) {
        formEl.scrollIntoView({ behavior: 'smooth', block: 'center' });
      }
    }
  }, true);

  // Scroll reveal observer for smooth entrance animations
  (function() {
    if (typeof window === 'undefined') return;
    
    var observer = new IntersectionObserver(function(entries) {
      entries.forEach(function(entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('is-visible');
          observer.unobserve(entry.target);
        }
      });
    }, { threshold: 0.08, rootMargin: '0px 0px -30px 0px' });

    function initReveal() {
      var elements = document.querySelectorAll('.mobile-only > div:not(#mobile-header), .desktop-only > div > div > div');
      elements.forEach(function(el) {
        if (!el.classList.contains('reveal-on-scroll')) {
          el.classList.add('reveal-on-scroll');
          observer.observe(el);
        }
      });
    }

    if (document.readyState === 'loading') {
      window.addEventListener('DOMContentLoaded', initReveal);
    } else {
      initReveal();
    }
    setTimeout(initReveal, 300);
  })();

  // Handle form submissions to redirect to thank you page
  (function() {
    function handleFormSubmit(e) {
      e.preventDefault();
      var form = e.target;
      var data = new FormData(form);
      var submitBtn = form.querySelector('button[type="submit"]');
      if (submitBtn) {
        submitBtn.disabled = true;
        var oldText = submitBtn.innerHTML;
        submitBtn.innerHTML = 'Submitting...';
      }
      fetch(form.action, {
        method: 'POST',
        body: data
      }).then(function() {
        window.location.href = 'https://lp.myhbinc.com/thank-you/';
      }).catch(function() {
        // Fallback in case fetch fails due to CORS or other issues
        window.location.href = 'https://lp.myhbinc.com/thank-you/';
      });
    }

    function attachFormHandlers() {
      var desktopForm = document.getElementById('estimate');
      var mobileForm = document.getElementById('lead-form');
      if (desktopForm) desktopForm.addEventListener('submit', handleFormSubmit);
      if (mobileForm) mobileForm.addEventListener('submit', handleFormSubmit);
    }

    if (document.readyState === 'loading') {
      window.addEventListener('DOMContentLoaded', attachFormHandlers);
    } else {
      attachFormHandlers();
    }
  })();
