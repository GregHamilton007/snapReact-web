---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

# layout: home
layout: default
title: algoci - Innovation Hub
---

<div class="hero">
  <div class="hero-content">
    <h1>Welcome to algoci</h1>
    <p class="lead">Empowering innovation through technology and data-driven solutions</p>
    <div class="hero-buttons">
      <a href="#projects" class="button primary">Explore Our Projects</a>
      <a href="/about-algoci" class="button secondary">About Us</a>
    </div>
  </div>
</div>

<div class="about-section">
  <div class="container">
    <h2>Who We Are</h2>
    <p>algoci is a forward-thinking technology company dedicated to creating innovative solutions that make a difference. We combine cutting-edge technology with deep domain expertise to deliver exceptional results for our clients and partners.</p>
  </div>
</div>

<div id="projects" class="projects-section">
  <div class="container">
    <h2 class="section-title">Our Projects</h2>
    <div class="projects-grid">
      <div class="project-card">
        <div class="project-icon">🗺️</div>
        <h3>JourneyHue</h3>
        <p>Interactive visualization of travel times and nearby amenities</p>
        <div class="project-tags">
          <span class="tag">Maps</span>
          <span class="tag">Real Estate</span>
          <span class="tag">Analytics</span>
        </div>
        <a href="/projects/journeyhue/" class="button">View Project</a>
      </div>

      <div class="project-card">
        <div class="project-icon">📊</div>
        <h3>Data Analytics Platform</h3>
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
        <h3>AI Solutions</h3>
        <p>Custom AI and machine learning solutions for your business needs</p>
        <div class="project-tags">
          <span class="tag">AI</span>
          <span class="tag">Machine Learning</span>
          <span class="tag">Automation</span>
        </div>
        <a href="#" class="button disabled">Coming Soon</a>
      </div>
    </div>
  </div>
</div>

<div class="contact-section">
  <div class="container">
    <h2>Get in Touch</h2>
    <p>Have questions or want to learn more about our services?</p>
    <a href="mailto:management@algoci.com" class="button primary">Email Us</a>
  </div>
</div>

<style>
:root {
  --primary-color: #2563eb;
  --secondary-color: #1e40af;
  --text-color: #1f2937;
  --text-light: #4b5563;
  --background-light: #f3f4f6;
  --background-white: #ffffff;
  --spacing-unit: 1rem;
}

body {
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  line-height: 1.6;
  color: var(--text-color);
  margin: 0;
  padding: 0;
}

.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 var(--spacing-unit);
}

.hero {
  background: linear-gradient(135deg, #f8fafc 0%, #e2e8f0 100%);
  padding: 8rem 0;
  position: relative;
  overflow: hidden;
}

.hero-content {
  max-width: 800px;
  margin: 0 auto;
  text-align: center;
  padding: 0 var(--spacing-unit);
}

.hero h1 {
  font-size: 4.5rem;
  font-weight: 800;
  margin-bottom: 1.5rem;
  color: var(--text-color);
  line-height: 1.2;
  letter-spacing: -0.02em;
}

.lead {
  font-size: 1.5rem;
  color: var(--text-light);
  max-width: 600px;
  margin: 0 auto 2.5rem;
  font-weight: 400;
}

.hero-buttons {
  display: flex;
  gap: 1rem;
  justify-content: center;
}

.button {
  display: inline-block;
  padding: 1rem 2rem;
  font-weight: 600;
  text-decoration: none;
  border-radius: 8px;
  transition: all 0.3s ease;
  font-size: 1rem;
}

.button.primary {
  background: var(--primary-color);
  color: white;
}

.button.secondary {
  background: transparent;
  border: 2px solid var(--primary-color);
  color: var(--primary-color);
}

.button:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
}

.button.primary:hover {
  background: var(--secondary-color);
}

.button.secondary:hover {
  background: var(--primary-color);
  color: white;
}

.button.disabled {
  background: #9ca3af;
  cursor: not-allowed;
  pointer-events: none;
}

.section-title {
  text-align: center;
  font-size: 2.5rem;
  font-weight: 700;
  margin-bottom: 3rem;
  color: var(--text-color);
}

.about-section {
  padding: 6rem 0;
  background: var(--background-white);
}

.about-section h2 {
  font-size: 2.5rem;
  font-weight: 700;
  margin-bottom: 1.5rem;
  text-align: center;
}

.about-section p {
  font-size: 1.25rem;
  color: var(--text-light);
  max-width: 800px;
  margin: 0 auto;
  text-align: center;
  line-height: 1.8;
}

.projects-section {
  padding: 6rem 0;
  background: var(--background-light);
}

.projects-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
  gap: 2rem;
  margin-top: 3rem;
}

.project-card {
  background: var(--background-white);
  border-radius: 16px;
  padding: 2.5rem;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
  transition: all 0.3s ease;
  display: flex;
  flex-direction: column;
  height: 100%;
}

.project-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 12px 24px rgba(0, 0, 0, 0.1);
}

.project-icon {
  font-size: 3rem;
  margin-bottom: 1.5rem;
}

.project-card h3 {
  font-size: 1.5rem;
  font-weight: 700;
  margin-bottom: 1rem;
  color: var(--text-color);
}

.project-card p {
  color: var(--text-light);
  margin-bottom: 1.5rem;
  flex-grow: 1;
  line-height: 1.6;
}

.project-tags {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
  margin-bottom: 1.5rem;
}

.tag {
  background: var(--background-light);
  color: var(--text-light);
  padding: 0.4rem 1rem;
  border-radius: 20px;
  font-size: 0.875rem;
  font-weight: 500;
}

.contact-section {
  padding: 6rem 0;
  background: var(--background-white);
  text-align: center;
}

.contact-section h2 {
  font-size: 2.5rem;
  font-weight: 700;
  margin-bottom: 1rem;
}

.contact-section p {
  font-size: 1.25rem;
  color: var(--text-light);
  margin-bottom: 2rem;
}

@media (max-width: 768px) {
  .hero h1 {
    font-size: 3rem;
  }
  
  .lead {
    font-size: 1.25rem;
  }
  
  .hero-buttons {
    flex-direction: column;
    align-items: center;
  }
  
  .button {
    width: 100%;
    max-width: 300px;
    text-align: center;
  }
  
  .projects-grid {
    grid-template-columns: 1fr;
  }
  
  .section-title {
    font-size: 2rem;
  }
}
</style>