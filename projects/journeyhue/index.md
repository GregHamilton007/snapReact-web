---
layout: default
title: JourneyHue - Interactive Travel Time Visualization
---

<!-- Add Firebase SDK -->
<script type="module">
  // Import the functions you need from the SDKs you need
  import { initializeApp } from "https://www.gstatic.com/firebasejs/10.8.0/firebase-app.js";
  import { getFirestore, collection, addDoc, serverTimestamp } from "https://www.gstatic.com/firebasejs/10.8.0/firebase-firestore.js";

  // Your web app's Firebase configuration
  const firebaseConfig = {
    apiKey: "AIzaSyAM6U2dy7EKF0ey1TO_YV_WmLZ7YbRUdO4",
    authDomain: "journeyhue.firebaseapp.com",
    projectId: "journeyhue",
    storageBucket: "journeyhue.firebasestorage.app",
    messagingSenderId: "551447445192",
    appId: "1:551447445192:web:31a99fc5bc3914be5a6ffd",
    measurementId: "G-PXY3M7PTNB"
  };

  // Initialize Firebase
  const app = initializeApp(firebaseConfig);
  const db = getFirestore(app);

  // Make Firebase available globally
  window.firebaseApp = app;
  window.firestore = db;

  // Initialize form submission handler
  document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('locationForm');
    if (form) {
      form.addEventListener('submit', async function(e) {
        e.preventDefault();
        
        const streetAddress = document.getElementById('streetAddress').value;
        const city = document.getElementById('city').value;
        const province = document.getElementById('province').value;
        const country = document.getElementById('country').value;
        const mode = document.getElementById('mode').value;

        // Track form submission
        console.log('Tracking form submission:', mode);
        gtag('event', 'location_submission', {
          'event_category': 'form',
          'event_label': mode,
          'value': 1
        });

        const fullAddress = `${streetAddress}, ${city}, ${province}, ${country}`;
        const subject = 'New Location Submission for JourneyHue';
        const body = `New location submission details:\n\nFull Address: ${fullAddress}\nTravel Mode: ${mode}`;
        
        try {
          // Store in Firestore
          await addDoc(collection(db, 'location_submissions'), {
            streetAddress,
            city,
            province,
            country,
            mode,
            fullAddress,
            timestamp: serverTimestamp()
          });

          const mailtoLink = `mailto:management@algoci.com?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(body)}`;
          window.location.href = mailtoLink;
          
          const statusDiv = document.getElementById('submissionStatus');
          statusDiv.textContent = 'Location submitted successfully! Opening email client...';
          statusDiv.className = 'submission-status success';
          form.reset();
        } catch (error) {
          console.error('Error storing location:', error);
          const statusDiv = document.getElementById('submissionStatus');
          statusDiv.textContent = 'Error submitting location. Please try again.';
          statusDiv.className = 'submission-status error';
        }
      });
    }
  });
</script>

<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-PXY3M7PTNB"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-PXY3M7PTNB');
</script>

<div class="project-header">
  <h1>JourneyHue</h1>
  <p class="lead">Interactive visualization of travel times and nearby amenities</p>
</div>

<div class="project-content">
  <section class="project-overview">
    <h2>Project Overview</h2>
    <p>JourneyHue is an innovative tool that helps users visualize travel times and discover nearby amenities for a given area. Using advanced mapping technology and real-time data, JourneyHue provides an intuitive interface for exploring accessibility and convenience factors in any location.</p>
  </section>

  <section class="features">
    <h2>Key Features</h2>
    <ul>
      <li>Interactive travel time heatmaps</li>
      <li>Nearby amenities discovery</li>
      <li>Customizable visualization options</li>
    </ul>
  </section>

  <section class="demo">
    <h2>Try It Out</h2>
    <p>Experience JourneyHue's capabilities with our interactive demo:</p>
    <div class="demo-container">
      <a href="/maps/travel_time_heatmap_driving_Wellington_St_Ottawa_ON_K1A_0A9.html" class="demo-link">
        View Driving Time Heatmap Demo
      </a>
      <a href="/maps/travel_time_heatmap_walking_Wellington_St_Ottawa_ON_K1A_0A9.html" class="demo-link" style="margin-left: 1rem;">
        View Walking Time Heatmap Demo
      </a>
    </div>
  </section>

  <section class="custom-request">
    <h2>Request a Custom Map</h2>
    <p> We can create a custom travel time heatmap for your area! Simply email us at <a href="mailto:management@algoci.com">management@algoci.com</a> with your desired location, and we'll do our best to generate a personalized map for you for free.</p>
  </section>

  <section class="location-submission">
    <h2>Submit a Location</h2>
    <p>Help us understand what locations are important to you! Submit an address you'd like to see analyzed:</p>
    <form id="locationForm" class="submission-form">
      <div class="form-group">
        <label for="streetAddress">Street Address:</label>
        <input type="text" id="streetAddress" name="streetAddress" required placeholder="e.g., 123 Main St">
      </div>
      <div class="form-group">
        <label for="city">City:</label>
        <input type="text" id="city" name="city" required placeholder="e.g., Ottawa">
      </div>
      <div class="form-group">
        <label for="province">Province/State:</label>
        <input type="text" id="province" name="province" required placeholder="e.g., ON">
      </div>
      <div class="form-group">
        <label for="country">Country:</label>
        <input type="text" id="country" name="country" required placeholder="e.g., Canada">
      </div>
      <div class="form-group">
        <label for="mode">Travel Mode:</label>
        <select id="mode" name="mode" required>
          <option value="driving">Driving</option>
          <option value="walking">Walking</option>
        </select>
      </div>
      <button type="submit" class="submit-button">Submit Location</button>
    </form>
    <div id="submissionStatus" class="submission-status"></div>
  </section>
</div>

<style>
.project-header {
  text-align: center;
  padding: 4rem 2rem;
  background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
  margin-bottom: 2rem;
}

.project-header h1 {
  font-size: 3rem;
  color: #2c3e50;
  margin-bottom: 1rem;
}

.lead {
  font-size: 1.5rem;
  color: #34495e;
  max-width: 800px;
  margin: 0 auto;
}

.project-content {
  max-width: 1000px;
  margin: 0 auto;
  padding: 2rem;
}

.project-overview, .features, .demo {
  margin-bottom: 3rem;
}

h2 {
  color: #2c3e50;
  margin-bottom: 1.5rem;
  font-size: 2rem;
}

.features ul {
  list-style-type: none;
  padding: 0;
}

.features li {
  padding: 0.5rem 0;
  color: #34495e;
  font-size: 1.1rem;
}

.features li:before {
  content: "•";
  color: #3498db;
  font-weight: bold;
  margin-right: 0.5rem;
}

.demo-container {
  background: #f8f9fa;
  padding: 2rem;
  border-radius: 8px;
  text-align: center;
}

.demo-link {
  display: inline-block;
  padding: 1rem 2rem;
  background-color: #3498db;
  color: white;
  text-decoration: none;
  border-radius: 4px;
  font-size: 1.1rem;
  transition: background-color 0.3s ease;
}

.demo-link:hover {
  background-color: #2980b9;
}

.coming-soon {
  color: #7f8c8d;
  font-style: italic;
}

@media (max-width: 768px) {
  .project-header h1 {
    font-size: 2.5rem;
  }
  
  .lead {
    font-size: 1.2rem;
  }
  
  .project-content {
    padding: 1rem;
  }
}

.location-submission {
  margin-top: 3rem;
  padding: 2rem;
  background: #f8f9fa;
  border-radius: 8px;
}

.submission-form {
  max-width: 600px;
  margin: 0 auto;
}

.form-group {
  margin-bottom: 1.5rem;
}

.form-group label {
  display: block;
  margin-bottom: 0.5rem;
  color: #2c3e50;
  font-weight: 500;
}

.form-group input,
.form-group select {
  width: 100%;
  padding: 0.75rem;
  border: 1px solid #ddd;
  border-radius: 4px;
  font-size: 1rem;
}

.submit-button {
  background-color: #3498db;
  color: white;
  padding: 1rem 2rem;
  border: none;
  border-radius: 4px;
  font-size: 1.1rem;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.submit-button:hover {
  background-color: #2980b9;
}

.submission-status {
  margin-top: 1rem;
  padding: 1rem;
  border-radius: 4px;
  text-align: center;
}

.submission-status.success {
  background-color: #d4edda;
  color: #155724;
}

.submission-status.error {
  background-color: #f8d7da;
  color: #721c24;
}
</style>

<script>
document.addEventListener('DOMContentLoaded', function() {
  // Track map page access
  function trackMapAccess() {
    const currentPath = window.location.pathname;
    if (currentPath.includes('/maps/')) {
      const mapType = currentPath.includes('driving') ? 'driving' : 'walking';
      // Extract the full address from the URL
      const urlParts = currentPath.split('/').pop().replace('.html', '').split('_');
      const address = urlParts.slice(3).join(' '); // Get everything after the first 3 parts
      const filename = currentPath.split('/').pop(); // Get the HTML filename
      
      gtag('event', 'map_access', {
        'event_category': 'maps',
        'event_label': `${mapType}_${address}`,
        'filename': filename,
        'value': 1
      });
      
      // Track map load time
      window.addEventListener('load', function() {
        const loadTime = performance.now();
        gtag('event', 'map_load_time', {
          'event_category': 'performance',
          'event_label': `${mapType}_${address}`,
          'filename': filename,
          'value': Math.round(loadTime)
        });
      });

      // Track map interactions
      if (typeof map !== 'undefined') {
        // Track panning
        map.on('moveend', function() {
          gtag('event', 'map_pan', {
            'event_category': 'map_interaction',
            'event_label': `${mapType}_${address}`,
            'center': map.getCenter().toString(),
            'zoom': map.getZoom()
          });
        });

        // Track zooming
        map.on('zoomend', function() {
          gtag('event', 'map_zoom', {
            'event_category': 'map_interaction',
            'event_label': `${mapType}_${address}`,
            'zoom_level': map.getZoom()
          });
        });

        // Track layer toggles
        document.querySelectorAll('.layer-toggle').forEach(toggle => {
          toggle.addEventListener('change', function() {
            gtag('event', 'layer_toggle', {
              'event_category': 'map_interaction',
              'event_label': `${mapType}_${address}`,
              'layer_name': this.name,
              'layer_state': this.checked ? 'on' : 'off'
            });
          });
        });

        // Track marker clicks
        map.on('click', function(e) {
          const features = map.queryRenderedFeatures(e.point);
          if (features.length > 0) {
            gtag('event', 'marker_click', {
              'event_category': 'map_interaction',
              'event_label': `${mapType}_${address}`,
              'feature_type': features[0].layer.id,
              'coordinates': e.lngLat.toString()
            });
          }
        });

        // Track heatmap opacity changes
        const opacitySlider = document.querySelector('input[type="range"]');
        if (opacitySlider) {
          opacitySlider.addEventListener('change', function() {
            gtag('event', 'heatmap_opacity_change', {
              'event_category': 'map_interaction',
              'event_label': `${mapType}_${address}`,
              'opacity_value': this.value
            });
          });
        }
      }
    }
  }

  // Call the tracking function when the page loads
  trackMapAccess();

  // Track time spent on page
  let startTime = Date.now();
  window.addEventListener('beforeunload', function() {
    const timeSpent = Math.round((Date.now() - startTime) / 1000);
    gtag('event', 'time_spent', {
      'event_category': 'engagement',
      'event_label': 'page_duration',
      'value': timeSpent
    });
  });

  // Track scroll depth
  let maxScroll = 0;
  window.addEventListener('scroll', function() {
    const scrollPercent = Math.round((window.scrollY + window.innerHeight) / document.documentElement.scrollHeight * 100);
    if (scrollPercent > maxScroll) {
      maxScroll = scrollPercent;
      if (maxScroll % 25 === 0) { // Track at 25%, 50%, 75%, 100%
        gtag('event', 'scroll_depth', {
          'event_category': 'engagement',
          'event_label': `${maxScroll}%`,
          'value': maxScroll
        });
      }
    }
  });

  // Track email link clicks
  document.querySelector('a[href^="mailto:"]').addEventListener('click', function() {
    gtag('event', 'email_click', {
      'event_category': 'contact',
      'event_label': 'custom_map_request'
    });
  });

  // Track section visibility using Intersection Observer
  const sections = document.querySelectorAll('section');
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        gtag('event', 'section_view', {
          'event_category': 'content',
          'event_label': entry.target.className
        });
      }
    });
  }, { threshold: 0.5 });

  sections.forEach(section => observer.observe(section));

  // Track feature list interactions
  document.querySelectorAll('.features li').forEach((feature, index) => {
    feature.addEventListener('click', function() {
      gtag('event', 'feature_click', {
        'event_category': 'features',
        'event_label': this.textContent.trim(),
        'value': index + 1
      });
    });
  });

  // Track demo link clicks
  document.querySelectorAll('.demo-link').forEach(link => {
    link.addEventListener('click', function(e) {
      const mode = this.textContent.includes('Driving') ? 'driving' : 'walking';
      console.log('Tracking demo click:', mode);
      gtag('event', 'demo_click', {
        'event_category': 'demo',
        'event_label': mode,
        'value': 1
      });
    });
  });

  // Verify GA is loaded
  console.log('Google Analytics loaded:', typeof gtag !== 'undefined');
});
</script> 