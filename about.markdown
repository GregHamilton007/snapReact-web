---
# layout: page
layout: post
title: About
permalink: /about/
---

This is the base Jekyll theme. You can find out more info about customizing your Jekyll theme, as well as basic Jekyll usage documentation at [jekyllrb.com](https://jekyllrb.com/)

You can find the source code for Minima at GitHub:
[jekyll][jekyll-organization] /
[minima](https://github.com/jekyll/minima)

You can find the source code for Jekyll at GitHub:
[jekyll][jekyll-organization] /
[jekyll](https://github.com/jekyll/jekyll)


[jekyll-organization]: https://github.com/jekyll

---
layout: default
title: About JourneyHue
---

<div class="about-container">
  <header class="about-header">
    <h1>About JourneyHue</h1>
    <p class="lead">Transforming how we understand and visualize travel possibilities</p>
  </header>

  <section class="about-section">
    <h2>Our Mission</h2>
    <p>At JourneyHue, we're dedicated to revolutionizing how people in the hospitality and housing market understand and communicate travel possibilities. Our interactive tools help visualize what's possible within specific time frames, making it easier to showcase the value of locations and properties.</p>
  </section>

  <section class="about-section">
    <h2>What We Do</h2>
    <div class="features-grid">
      <div class="feature-card">
        <h3>Interactive Heatmaps</h3>
        <p>Create dynamic visualizations of travel times and accessibility for any location.</p>
      </div>
      <div class="feature-card">
        <h3>Location Analytics</h3>
        <p>Analyze and understand the value of locations based on travel times and nearby amenities.</p>
      </div>
      <div class="feature-card">
        <h3>Custom Solutions</h3>
        <p>Tailored tools for real estate, hospitality, and urban planning professionals.</p>
      </div>
    </div>
  </section>

  <section class="about-section">
    <h2>Our Technology</h2>
    <p>We leverage cutting-edge mapping and data visualization technologies to create intuitive, powerful tools that help our users make better decisions about locations and properties.</p>
  </section>

  <section class="about-section">
    <h2>Get Started</h2>
    <p>Ready to transform how you visualize and communicate travel possibilities? Explore our tools and see how JourneyHue can help you showcase the value of your locations.</p>
    <div class="cta-buttons">
      <a href="/" class="button primary">View Our Tools</a>
      <a href="mailto:contact@journeyhue.com" class="button secondary">Contact Us</a>
    </div>
  </section>
</div>

<style>
.about-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 2rem;
}

.about-header {
  text-align: center;
  margin-bottom: 4rem;
}

.about-header h1 {
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

.about-section {
  margin-bottom: 4rem;
}

.about-section h2 {
  color: #2c3e50;
  margin-bottom: 1.5rem;
  font-size: 2rem;
}

.about-section p {
  color: #34495e;
  line-height: 1.6;
  margin-bottom: 1.5rem;
}

.features-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 2rem;
  margin-top: 2rem;
}

.feature-card {
  background: #f8f9fa;
  padding: 2rem;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

.feature-card h3 {
  color: #2c3e50;
  margin-bottom: 1rem;
}

.cta-buttons {
  display: flex;
  gap: 1rem;
  margin-top: 2rem;
}

.button {
  display: inline-block;
  padding: 0.8rem 1.5rem;
  border-radius: 4px;
  text-decoration: none;
  transition: all 0.2s;
}

.button.primary {
  background: #3498db;
  color: white;
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

@media (max-width: 768px) {
  .about-header h1 {
    font-size: 2.5rem;
  }
  
  .lead {
    font-size: 1.2rem;
  }
  
  .cta-buttons {
    flex-direction: column;
  }
  
  .features-grid {
    grid-template-columns: 1fr;
  }
}
</style>
