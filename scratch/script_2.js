
  (function() {
    var track = document.getElementById('step-track');
    var nodes = document.querySelectorAll('.step-timeline-node');
    var progressLine = document.getElementById('step-active-line');
    var prevBtn = document.getElementById('step-prev-btn');
    var nextBtn = document.getElementById('step-next-btn');

    if (!track || nodes.length === 0 || !progressLine) return;

    var currentIndex = 0;
    var slideWidth = 420;
    var totalSlides = nodes.length;

    function updateSlider(index) {
      currentIndex = index;
      
      // Slide movement
      track.style.transform = 'translateX(' + (-currentIndex * slideWidth) + 'px)';
      
      // Update active progress line width (percentage between nodes)
      // Node 0 -> 0%, Node 4 -> 100%
      var percent = (currentIndex / (totalSlides - 1)) * 100;
      progressLine.style.width = percent + '%';
      
      // Update nodes styling
      nodes.forEach(function(node, idx) {
        var ring = node.querySelector('.step-node-ring');
        var dot = node.querySelector('.step-node-dot');
        var label = node.querySelector('.step-node-label');
        
        if (idx === currentIndex) {
          ring.style.border = '2px solid #007BC3';
          dot.style.backgroundColor = '#007BC3';
          label.style.color = '#007BC3';
        } else if (idx < currentIndex) {
          // Completed steps
          ring.style.border = '2px solid #007BC3';
          dot.style.backgroundColor = '#007BC3';
          label.style.color = '#7E7E7E';
        } else {
          // Future steps
          ring.style.border = '2px solid #cccccc';
          dot.style.backgroundColor = '#cccccc';
          label.style.color = '#7E7E7E';
        }
      });

      // Update button visual states
      if (prevBtn) {
        if (currentIndex === 0) {
          prevBtn.style.opacity = '0.5';
          prevBtn.style.cursor = 'not-allowed';
        } else {
          prevBtn.style.opacity = '1';
          prevBtn.style.cursor = 'pointer';
        }
      }

      if (nextBtn) {
        if (currentIndex === totalSlides - 1) {
          nextBtn.style.opacity = '0.5';
          nextBtn.style.cursor = 'not-allowed';
        } else {
          nextBtn.style.opacity = '1';
          nextBtn.style.cursor = 'pointer';
        }
      }
    }

    // Set initial active state
    updateSlider(0);

    // Node click events
    nodes.forEach(function(node) {
      node.addEventListener('click', function() {
        var index = parseInt(node.getAttribute('data-index'), 10);
        updateSlider(index);
      });
    });

    // Arrow button click events
    if (prevBtn) {
      prevBtn.addEventListener('click', function() {
        if (currentIndex > 0) {
          updateSlider(currentIndex - 1);
        }
      });
    }

    if (nextBtn) {
      nextBtn.addEventListener('click', function() {
        if (currentIndex < totalSlides - 1) {
          updateSlider(currentIndex + 1);
        }
      });
    }
  })();
