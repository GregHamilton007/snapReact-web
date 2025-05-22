---
layout: default
title: JourneyHue - Interactive Travel Time Visualization
---

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
        <label for="address">Address:</label>
        <input type="text" id="address" name="address" required placeholder="e.g., 123 Main St, Ottawa">
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
document.getElementById('locationForm').addEventListener('submit', function(e) {
  e.preventDefault();
  
  const address = document.getElementById('address').value;
  const mode = document.getElementById('mode').value;

  const subject = 'New Location Submission for JourneyHue';
  const body = `New location submission details:\n\nAddress: ${address}\nTravel Mode: ${mode}`;
  
  const mailtoLink = `mailto:management@algoci.com?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(body)}`;
  
  window.location.href = mailtoLink;
  
  const statusDiv = document.getElementById('submissionStatus');
  statusDiv.textContent = 'Opening email client...';
  statusDiv.className = 'submission-status success';
  document.getElementById('locationForm').reset();
});
</script> 