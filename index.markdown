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
    <a href="/projects/lucid-dreaming/" class="button primary">Read the Lucid Dreaming Book</a>
    <a href="#projects" class="button secondary">Explore Our Projects</a>
  </div>
</div>

<div class="featured-book">
  <div class="featured-book-copy">
    <p class="featured-label">Featured Resource</p>
    <h2>The Art and Science of Lucid Dreaming</h2>
    <p>Learn how to lucid dream with a free full-length book and audiobook by Ryan Hamilton. The guide covers dream recall, reality checks, MILD, WBTB, WILD, dream incubation, stabilization, and sleep quality.</p>
    <div class="featured-book-actions">
      <a href="/projects/lucid-dreaming/" class="button primary">Open Book Page</a>
      <a href="/how-to-lucid-dream/" class="button secondary">How to Lucid Dream</a>
    </div>
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
    <a href="/projects/journeyhue/" class="button">View Project</a>
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

  <div class="project-card">
    <div class="project-icon">📖</div>
    <h2>The Art and Science of Lucid Dreaming</h2>
    <p>A free lucid dreaming book and audiobook with step-by-step guidance for people learning how to lucid dream</p>
    <div class="project-tags">
      <span class="tag">Book</span>
      <span class="tag">Audiobook</span>
      <span class="tag">Lucid Dreaming</span>
    </div>
    <a href="/projects/lucid-dreaming/" class="button">View Book</a>
  </div>
</div>

<div class="contact-section">
  <h2>Get in Touch</h2>
  <p>Have questions or want to learn more about our services?</p>
  <a href="mailto:management@algoci.com" class="button primary">Email Us</a>
</div>

<div class="feedback-section">
  <div class="feedback-card">
    <p class="featured-label">Share Feedback</p>
    <h2>Suggest Improvements or Send Comments to the Author</h2>
    <p class="feedback-intro">Have an idea, correction, or note for Ryan Hamilton? Send it here. If you want a reply, you can include your email address.</p>
    <form id="authorFeedbackForm" class="feedback-form">
      <div class="form-group">
        <label for="feedback-name">Name</label>
        <input type="text" id="feedback-name" name="name" placeholder="Your name">
      </div>
      <div class="form-group">
        <label for="feedback-email">Email for a response (optional)</label>
        <input type="email" id="feedback-email" name="email" placeholder="you@example.com">
      </div>
      <div class="form-group">
        <label for="feedback-message">Improvements and comments</label>
        <textarea id="feedback-message" name="message" rows="6" maxlength="1200" placeholder="Share your feedback for the author..." required></textarea>
      </div>
      <button type="submit" class="button primary">Send Feedback</button>
      <p id="feedback-status" class="feedback-status" aria-live="polite"></p>
    </form>
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

.featured-book {
  max-width: 1100px;
  margin: 0 auto;
  padding: 0 2rem 2rem;
}

.featured-book-copy {
  background: linear-gradient(135deg, #fff8e8 0%, #eef6ff 100%);
  border: 1px solid #d8e4f0;
  border-radius: 20px;
  padding: 2rem;
  box-shadow: 0 16px 40px rgba(21, 50, 75, 0.08);
}

.featured-label {
  text-transform: uppercase;
  letter-spacing: 0.12rem;
  font-size: 0.8rem;
  color: #2f6a9d;
  margin-bottom: 0.75rem;
}

.featured-book-copy h2 {
  margin-bottom: 0.75rem;
}

.featured-book-copy p {
  color: #34495e;
  font-size: 1.08rem;
  line-height: 1.7;
  max-width: 780px;
}

.featured-book-actions {
  display: flex;
  gap: 1rem;
  flex-wrap: wrap;
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

.contact-section {
  text-align: center;
  padding: 4rem 2rem;
  background: #f8f9fa;
  margin-top: 2rem;
}

.contact-section h2 {
  color: #2c3e50;
  margin-bottom: 1rem;
  font-size: 2.5rem;
}

.contact-section p {
  color: #34495e;
  font-size: 1.2rem;
  margin-bottom: 2rem;
}

.feedback-section {
  padding: 2rem;
}

.feedback-card {
  max-width: 900px;
  margin: 0 auto;
  padding: 2.5rem;
  background: linear-gradient(180deg, #ffffff 0%, #f7fbff 100%);
  border: 1px solid #d7e5f2;
  border-radius: 18px;
  box-shadow: 0 18px 40px rgba(31, 61, 93, 0.08);
}

.feedback-card h2 {
  margin-bottom: 0.75rem;
  color: #1f3d5d;
}

.feedback-intro {
  color: #526577;
  margin-bottom: 1.75rem;
}

.feedback-form {
  display: grid;
  gap: 1rem;
}

.form-group {
  display: grid;
  gap: 0.45rem;
}

.form-group label {
  font-weight: 600;
  color: #2c3e50;
}

.form-group input,
.form-group textarea {
  width: 100%;
  padding: 0.9rem 1rem;
  border: 1px solid #c8d6e5;
  border-radius: 10px;
  font: inherit;
  color: #2c3e50;
  background: #fff;
  box-sizing: border-box;
}

.form-group input:focus,
.form-group textarea:focus {
  outline: none;
  border-color: #3498db;
  box-shadow: 0 0 0 3px rgba(52, 152, 219, 0.15);
}

.feedback-status {
  min-height: 1.5rem;
  margin: 0;
  color: #526577;
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

  .feedback-card {
    padding: 1.5rem;
  }
}
</style>

<script>
document.addEventListener('DOMContentLoaded', function () {
  const form = document.getElementById('authorFeedbackForm');
  const status = document.getElementById('feedback-status');

  if (!form || !status) {
    return;
  }

  form.addEventListener('submit', function (event) {
    event.preventDefault();

    const formData = new FormData(form);
    const name = String(formData.get('name') || '').trim();
    const email = String(formData.get('email') || '').trim();
    const message = String(formData.get('message') || '').trim();

    if (!message) {
      status.textContent = 'Please add your feedback before sending.';
      return;
    }

    const lines = [
      'Feedback for Ryan Hamilton',
      '',
      'Name: ' + (name || 'Not provided'),
      'Email for response: ' + (email || 'Not provided'),
      '',
      'Comments and improvements:',
      message
    ];

    const subject = encodeURIComponent('Website feedback for the author');
    const body = encodeURIComponent(lines.join('\n'));
    window.location.href = 'mailto:management@algoci.com?subject=' + subject + '&body=' + body;
    status.textContent = 'Your email app should open with the feedback message ready to send.';
  });
});
</script>
