---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

# layout: home
layout: default
title: JourneyHue - Interactive Travel Time Visualization
---

<div class="hero">
  <h1>JourneyHue</h1>
  <p class="lead">Visualizing travel possibilities and nearby amenities for the hospitality and housing market</p>
  <div class="hero-buttons">
    <a href="#projects" class="button primary">View Projects</a>
    <a href="/about" class="button secondary">Learn More</a>
  </div>
</div>

<div id="projects" class="projects-grid">
  <div class="project-card">
    <div class="project-icon">🗺️</div>
    <h2>Travel Time Heatmap</h2>
    <p>Interactive visualization of travel times and nearby amenities</p>
    <div class="project-tags">
      <span class="tag">Maps</span>
      <span class="tag">Real Estate</span>
      <span class="tag">Analytics</span>
    </div>
    <a href="/projects/travel-time-heatmap" class="button">View Project</a>
  </div>
  
  <div class="project-card coming-soon">
    <div class="project-icon">🏨</div>
    <h2>Hotel Analytics</h2>
    <p>Coming soon: Advanced analytics for hotel locations and amenities</p>
    <div class="project-tags">
      <span class="tag">Hotels</span>
      <span class="tag">Analytics</span>
      <span class="tag">Coming Soon</span>
    </div>
    <button class="button disabled">Coming Soon</button>
  </div>

  <div class="project-card coming-soon">
    <div class="project-icon">🏠</div>
    <h2>Property Insights</h2>
    <p>Coming soon: Deep insights into property locations and neighborhood data</p>
    <div class="project-tags">
      <span class="tag">Real Estate</span>
      <span class="tag">Analytics</span>
      <span class="tag">Coming Soon</span>
    </div>
    <button class="button disabled">Coming Soon</button>
  </div>
</div>

<style>
.hero {
  text-align: center;
  padding: 6rem 2rem;
  background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
  margin-bottom: 2rem;
}

.hero h1 {
  font-size: 4rem;
  margin-bottom: 1rem;
  color: #2c3e50;
}

.lead {
  font-size: 1.5rem;
  color: #34495e;
  max-width: 800px;
  margin: 0 auto 2rem;
}

.hero-buttons {
  display: flex;
  gap: 1rem;
  justify-content: center;
}

.button {
  display: inline-block;
  padding: 0.8rem 1.5rem;
  background: #3498db;
  color: white;
  text-decoration: none;
  border-radius: 4px;
  margin-top: 1rem;
  transition: all 0.2s;
  border: none;
  cursor: pointer;
}

.button.primary {
  background: #3498db;
}

.button.secondary {
  background: transparent;
  border: 2px solid #3498db;
  color: #3498db;
}

.button:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 8px rgba(0,0,0,0.1);
}

.button.disabled {
  background: #95a5a6;
  cursor: not-allowed;
}

.projects-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 2rem;
  padding: 2rem;
  max-width: 1200px;
  margin: 0 auto;
}

.project-card {
  background: white;
  border-radius: 12px;
  padding: 2rem;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  transition: all 0.3s;
  display: flex;
  flex-direction: column;
}

.project-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 8px 12px rgba(0, 0, 0, 0.15);
}

.project-icon {
  font-size: 2.5rem;
  margin-bottom: 1rem;
}

.project-card h2 {
  color: #2c3e50;
  margin-bottom: 0.5rem;
}

.project-card p {
  color: #7f8c8d;
  margin-bottom: 1rem;
  flex-grow: 1;
}

.project-tags {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
  margin-bottom: 1rem;
}

.tag {
  background: #f0f2f5;
  color: #34495e;
  padding: 0.3rem 0.8rem;
  border-radius: 20px;
  font-size: 0.9rem;
}

.coming-soon {
  opacity: 0.8;
}

@media (max-width: 768px) {
  .hero h1 {
    font-size: 3rem;
  }
  
  .lead {
    font-size: 1.2rem;
  }
  
  .hero-buttons {
    flex-direction: column;
  }
  
  .projects-grid {
    grid-template-columns: 1fr;
  }
}
</style>