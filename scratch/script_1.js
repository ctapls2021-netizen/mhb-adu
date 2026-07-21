
  (function() {
    var track = document.getElementById('adu-track');
    var dots = document.querySelectorAll('.adu-dot');
    if (!track || dots.length === 0) return;

    var currentIndex = 0;
    var slideWidth = 420;
    var totalSlides = dots.length;
    var autoSlideInterval;

    function updateSlider(index) {
      currentIndex = index;
      track.style.transform = 'translateX(' + (-currentIndex * slideWidth) + 'px)';
      
      // Update dots style
      dots.forEach(function(dot, idx) {
        if (idx === currentIndex) {
          dot.style.backgroundColor = '#0071c8';
        } else {
          dot.style.backgroundColor = '#cccccc';
        }
      });
    }

    // Set first dot as active initially
    updateSlider(0);

    // Click handlers for dots
    dots.forEach(function(dot) {
      dot.addEventListener('click', function() {
        var index = parseInt(dot.getAttribute('data-index'), 10);
        updateSlider(index);
        resetAutoSlide();
      });
    });

    // Auto-slide functionality
    function startAutoSlide() {
      autoSlideInterval = setInterval(function() {
        var nextIndex = (currentIndex + 1) % totalSlides;
        updateSlider(nextIndex);
      }, 4000);
    }

    function resetAutoSlide() {
      clearInterval(autoSlideInterval);
      startAutoSlide();
    }

    startAutoSlide();
  })();
