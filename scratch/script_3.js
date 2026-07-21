
  (function() {
    var track = document.getElementById('testi-track');
    var dots = document.querySelectorAll('.testi-dot');
    if (!track || dots.length === 0) return;

    var currentIndex = 0;
    var slideWidth = 420;
    var totalSlides = dots.length;

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
      });
    });
  })();
