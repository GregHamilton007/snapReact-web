---
layout: default
title: The Art and Science of Lucid Dreaming
---

<div class="project-header">
  <h1>The Art and Science of Lucid Dreaming</h1>
  <p class="lead">A practical guide to becoming aware in your dreams — by Ryan Hamilton</p>
</div>

<div class="project-content">
  <section class="project-overview">
    <h2>About the Book</h2>
    <p>Lucid dreaming is the experience of knowing you are dreaming while still asleep. This book walks you through the foundations step by step: building dream recall, training daytime awareness, using proven techniques like MILD and WBTB, and integrating lucid dreaming into a sustainable practice.</p>
    <p>Whether you are curious about consciousness, want to approach nightmares differently, or simply want your nights to feel less forgotten, this guide is designed to help you build the conditions that make lucid dreaming more likely over time.</p>
  </section>

  <section class="read-pdf">
    <h2>Read the PDF</h2>
    <p>Download or read the full book in your browser.</p>
    <div class="demo-container">
      <a href="/assets/lucid-dreaming/pdf/the-art-and-science-of-lucid-dreaming.pdf" class="demo-link" download>
        Download PDF
      </a>
      <a href="/assets/lucid-dreaming/pdf/the-art-and-science-of-lucid-dreaming.pdf" class="demo-link secondary" target="_blank" rel="noopener">
        Open in New Tab
      </a>
    </div>
    <div class="pdf-viewer">
      <embed
        src="/assets/lucid-dreaming/pdf/the-art-and-science-of-lucid-dreaming.pdf"
        type="application/pdf"
        width="100%"
        height="600px"
      />
    </div>
  </section>

  <section class="audiobook">
    <h2>Listen to the Audiobook</h2>
    <p>Stream the full audiobook by chapter (~5 hours total). Each track loads on demand — only the chapter you play is downloaded.</p>
    <div class="chapter-list">
      {% for chapter in site.data.lucid_dreaming_chapters %}
      <div class="chapter-item">
        <h3 class="chapter-title">{{ chapter.title }}</h3>
        <audio controls preload="none" src="/assets/lucid-dreaming/audio/{{ chapter.file }}">
          Your browser does not support the audio element.
        </audio>
      </div>
      {% endfor %}
    </div>
  </section>

  <section class="back-link">
    <a href="/" class="demo-link">Back to algoci</a>
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

.project-overview,
.read-pdf,
.audiobook,
.back-link {
  margin-bottom: 3rem;
}

h2 {
  color: #2c3e50;
  margin-bottom: 1.5rem;
  font-size: 2rem;
}

.project-overview p {
  color: #34495e;
  font-size: 1.1rem;
  line-height: 1.6;
  margin-bottom: 1rem;
}

.demo-container {
  background: #f8f9fa;
  padding: 2rem;
  border-radius: 8px;
  text-align: center;
  display: flex;
  gap: 1rem;
  justify-content: center;
  flex-wrap: wrap;
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

.demo-link.secondary {
  background-color: transparent;
  border: 2px solid #3498db;
  color: #3498db;
}

.demo-link.secondary:hover {
  background-color: #3498db;
  color: white;
}

.pdf-viewer {
  margin-top: 2rem;
  border-radius: 8px;
  overflow: hidden;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.audiobook p {
  color: #34495e;
  font-size: 1.1rem;
  margin-bottom: 1.5rem;
}

.chapter-list {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

.chapter-item {
  background: #f8f9fa;
  padding: 1.25rem 1.5rem;
  border-radius: 8px;
}

.chapter-title {
  color: #2c3e50;
  font-size: 1.1rem;
  margin: 0 0 0.75rem;
  font-weight: 600;
}

.chapter-item audio {
  width: 100%;
  height: 40px;
}

.back-link {
  text-align: center;
  padding-top: 1rem;
}

@media (max-width: 768px) {
  .project-header h1 {
    font-size: 2rem;
  }

  .lead {
    font-size: 1.2rem;
  }

  .pdf-viewer embed {
    height: 400px;
  }
}
</style>
