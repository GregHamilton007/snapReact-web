---
layout: default
title: JourneyHue - Interactive Travel Time Visualization
---

<div class="project-hero">
    <h1>JourneyHue</h1>
    <p class="lead">Interactive visualization of travel times and nearby amenities</p>
    <div class="project-meta">
        <span class="tag">Maps</span>
        <span class="tag">Real Estate</span>
        <span class="tag">Analytics</span>
    </div>
</div>

<div class="project-content">
    <section class="project-overview">
        <h2>Project Overview</h2>
        <p>JourneyHue is an innovative mapping solution that helps users visualize travel times and discover nearby
            amenities in an intuitive, color-coded interface. Perfect for real estate professionals, urban planners, and
            anyone interested in understanding location accessibility.</p>
    </section>

    <section class="project-features">
        <h2>Key Features</h2>
        <div class="features-grid">
            <div class="feature-card">
                <div class="feature-icon">⏱️</div>
                <h3>Travel Time Analysis</h3>
                <p>Visualize travel times to key destinations using an intuitive color gradient system</p>
            </div>
            <div class="feature-card">
                <div class="feature-icon">🏪</div>
                <h3>Amenity Discovery</h3>
                <p>Easily identify nearby points of interest, services, and facilities</p>
            </div>
            <div class="feature-card">
                <div class="feature-icon">📊</div>
                <h3>Data Insights</h3>
                <p>Access detailed analytics about location accessibility and amenity distribution</p>
            </div>
        </div>
    </section>

    <section class="project-demo">
        <h2>Interactive Demo</h2>
        <div class="demo-container">
            <p>Experience JourneyHue in action. Our interactive demo allows you to explore the features and capabilities
                of our platform.</p>
            <a href="/projects/JourneyHue/demo" class="button primary">Launch Demo</a>
        </div>
    </section>

    <section class="project-contact">
        <h2>Get Started</h2>
        <p>Ready to transform how you analyze and visualize location data? Contact us to learn more about implementing
            JourneyHue for your needs.</p>
        <a href="/contact" class="button secondary">Contact Us</a>
    </section>
</div>

<style>
    .project-hero {
        text-align: center;
        padding: 4rem 2rem;
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        margin-bottom: 2rem;
    }

    .project-hero h1 {
        font-size: 3.5rem;
        margin-bottom: 1rem;
        color: #2c3e50;
    }

    .project-meta {
        display: flex;
        gap: 1rem;
        justify-content: center;
        margin-top: 1.5rem;
    }

    .project-content {
        max-width: 1200px;
        margin: 0 auto;
        padding: 2rem;
    }

    .project-overview {
        text-align: center;
        margin-bottom: 4rem;
    }

    .project-overview p {
        font-size: 1.2rem;
        line-height: 1.6;
        color: #34495e;
        max-width: 800px;
        margin: 0 auto;
    }

    .features-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
        gap: 2rem;
        margin: 2rem 0;
    }

    .feature-card {
        background: white;
        padding: 2rem;
        border-radius: 12px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        text-align: center;
        transition: transform 0.3s;
    }

    .feature-card:hover {
        transform: translateY(-5px);
    }

    .feature-icon {
        font-size: 2.5rem;
        margin-bottom: 1rem;
    }

    .feature-card h3 {
        color: #2c3e50;
        margin-bottom: 1rem;
    }

    .project-demo,
    .project-contact {
        text-align: center;
        padding: 4rem 0;
        border-top: 1px solid #eee;
    }

    .demo-container {
        max-width: 600px;
        margin: 0 auto;
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
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }

    .tag {
        background: #f0f2f5;
        color: #34495e;
        padding: 0.3rem 0.8rem;
        border-radius: 20px;
        font-size: 0.9rem;
    }

    @media (max-width: 768px) {
        .project-hero h1 {
            font-size: 2.5rem;
        }

        .features-grid {
            grid-template-columns: 1fr;
        }

        .project-content {
            padding: 1rem;
        }
    }
</style>