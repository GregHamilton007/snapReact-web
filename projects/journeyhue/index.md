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
</style> 