---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

# layout: home
layout: default
title: algoci - Innovation Hub
---

<div class="hero">
  <h1>Welcome to algoci</h1>
  <p class="lead">Empowering innovation through technology and data-driven solutions</p>
  <div class="hero-buttons">
    <a href="#projects" class="button primary">Explore Our Projects</a>
    <a href="/about-algoci" class="button secondary">About Us</a>
  </div>
</div>

<div class="about-section">
  <h2>Who We Are</h2>
  <p>algoci is a forward-thinking technology company dedicated to creating innovative solutions that make a difference. We combine cutting-edge technology with deep domain expertise to deliver exceptional results for our clients and partners.</p>
</div>

<div id="projects" class="projects-grid">
  <div class="project-card">
    <div class="project-icon">🗺️</div>
    <h2>JourneyHue</h2>
    <p>Interactive visualization of travel times and nearby amenities</p>
    <div class="project-tags">
      <span class="tag">Maps</span>
      <span class="tag">Real Estate</span>
      <span class="tag">Analytics</span>
    </div>
    <a href="/_projects/JourneyHue/home.md" class="button">View Project</a>
  </div>

  <div class="project-card">
    <div class="project-icon">📊</div>
    <h2>Data Analytics Platform</h2>
    <p>Advanced analytics and visualization tools for business intelligence</p>
    <div class="project-tags">
      <span class="tag">Analytics</span>
      <span class="tag">Business Intelligence</span>
      <span class="tag">Data Science</span>
    </div>
    <a href="#" class="button disabled">Coming Soon</a>
  </div>

  <div class="project-card">
    <div class="project-icon">🤖</div>
    <h2>AI Solutions</h2>
    <p>Custom AI and machine learning solutions for your business needs</p>
    <div class="project-tags">
      <span class="tag">AI</span>
      <span class="tag">Machine Learning</span>
      <span class="tag">Automation</span>
    </div>
    <a href="#" class="button disabled">Coming Soon</a>
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

.about-section {
  max-width: 800px;
  margin: 0 auto;
  padding: 4rem 2rem;
  text-align: center;
}

.about-section h2 {
  color: #2c3e50;
  margin-bottom: 1.5rem;
  font-size: 2.5rem;
}

.about-section p {
  color: #34495e;
  font-size: 1.2rem;
  line-height: 1.6;
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