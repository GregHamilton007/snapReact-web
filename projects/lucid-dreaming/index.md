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

  <section class="reviews-section" aria-labelledby="reviews-heading">
    <div class="reviews-header">
      <div>
        <h2 id="reviews-heading">Reader Reviews</h2>
        <p>Share what resonated, what helped, or how the book landed for you.</p>
      </div>
      <div class="review-summary" aria-live="polite">
        <div class="rating-pill">
          <span class="rating-value" id="average-rating">4.8</span>
          <span class="rating-stars" id="average-rating-stars" aria-hidden="true">★★★★★</span>
        </div>
        <p class="rating-meta"><span id="review-count">2</span> reader reviews</p>
      </div>
    </div>

    <div class="reviews-grid">
      <div class="review-form-card">
        <h3>Leave a Review</h3>
        <form id="review-form" class="review-form">
          <label for="review-name">Name</label>
          <input id="review-name" name="name" type="text" maxlength="60" placeholder="Your name" required />

          <fieldset class="rating-fieldset">
            <legend>Your rating</legend>
            <div class="star-rating" role="radiogroup" aria-label="Book rating">
              <input id="rating-5" name="rating" type="radio" value="5" required />
              <label for="rating-5" aria-label="5 stars">★</label>
              <input id="rating-4" name="rating" type="radio" value="4" />
              <label for="rating-4" aria-label="4 stars">★</label>
              <input id="rating-3" name="rating" type="radio" value="3" />
              <label for="rating-3" aria-label="3 stars">★</label>
              <input id="rating-2" name="rating" type="radio" value="2" />
              <label for="rating-2" aria-label="2 stars">★</label>
              <input id="rating-1" name="rating" type="radio" value="1" />
              <label for="rating-1" aria-label="1 star">★</label>
            </div>
          </fieldset>

          <label for="review-title">Headline</label>
          <input id="review-title" name="title" type="text" maxlength="80" placeholder="A short summary of your review" required />

          <label for="review-comment">Comment</label>
          <textarea id="review-comment" name="comment" rows="5" maxlength="600" placeholder="What stood out to you?" required></textarea>

          <button type="submit" class="demo-link review-submit">Post Review</button>
          <p class="review-form-note" id="review-feedback" aria-live="polite"></p>
        </form>
      </div>

      <div class="review-list-card">
        <div class="review-list-header">
          <h3>What Readers Are Saying</h3>
          <button type="button" id="refresh-reviews" class="text-button">Refresh reviews</button>
        </div>
        <div id="reviews-list" class="reviews-list"></div>
      </div>
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
.reviews-section,
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

.reviews-section {
  background: linear-gradient(180deg, #f8fbff 0%, #eef4fb 100%);
  border: 1px solid #d6e3f0;
  border-radius: 18px;
  padding: 2rem;
}

.reviews-header {
  display: flex;
  justify-content: space-between;
  gap: 1.5rem;
  align-items: end;
  margin-bottom: 1.5rem;
}

.reviews-header p,
.rating-meta,
.review-form-note {
  color: #58708a;
}

.review-summary {
  background: white;
  border-radius: 14px;
  padding: 1rem 1.25rem;
  min-width: 190px;
  box-shadow: 0 10px 30px rgba(52, 73, 94, 0.08);
}

.rating-pill {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  margin-bottom: 0.25rem;
}

.rating-value {
  font-size: 2.2rem;
  line-height: 1;
  font-weight: 700;
  color: #15324b;
}

.rating-stars {
  letter-spacing: 0.15rem;
  color: #f4b942;
  font-size: 1.1rem;
}

.reviews-grid {
  display: grid;
  grid-template-columns: minmax(280px, 360px) minmax(0, 1fr);
  gap: 1.5rem;
}

.review-form-card,
.review-list-card {
  background: rgba(255, 255, 255, 0.86);
  border-radius: 16px;
  padding: 1.5rem;
  box-shadow: 0 14px 40px rgba(52, 73, 94, 0.07);
}

.review-form,
.review-list-card {
  display: flex;
  flex-direction: column;
}

.review-form label,
.rating-fieldset legend {
  color: #15324b;
  font-weight: 600;
  margin-bottom: 0.45rem;
}

.review-form input[type="text"],
.review-form textarea {
  width: 100%;
  box-sizing: border-box;
  border: 1px solid #c5d6e8;
  border-radius: 10px;
  padding: 0.85rem 0.95rem;
  font-size: 1rem;
  color: #24415a;
  background: white;
  margin-bottom: 1rem;
}

.review-form input[type="text"]:focus,
.review-form textarea:focus {
  outline: 2px solid rgba(52, 152, 219, 0.22);
  border-color: #3498db;
}

.rating-fieldset {
  border: none;
  padding: 0;
  margin: 0 0 1rem;
}

.star-rating {
  display: inline-flex;
  flex-direction: row-reverse;
  gap: 0.15rem;
}

.star-rating input {
  position: absolute;
  opacity: 0;
  pointer-events: none;
}

.star-rating label {
  font-size: 2rem;
  color: #c7d3df;
  cursor: pointer;
  line-height: 1;
  transition: color 0.2s ease, transform 0.2s ease;
}

.star-rating label:hover,
.star-rating label:hover ~ label,
.star-rating input:checked ~ label {
  color: #f4b942;
}

.star-rating label:hover {
  transform: translateY(-1px);
}

.review-submit {
  width: 100%;
  text-align: center;
}

.review-list-header {
  display: flex;
  justify-content: space-between;
  gap: 1rem;
  align-items: center;
  margin-bottom: 1rem;
}

.text-button {
  border: none;
  background: none;
  color: #2f7bb8;
  cursor: pointer;
  padding: 0;
  font-size: 0.95rem;
}

.text-button:hover {
  color: #1f5f91;
  text-decoration: underline;
}

.reviews-list {
  display: grid;
  gap: 1rem;
}

.review-card {
  background: white;
  border: 1px solid #dbe6f1;
  border-radius: 14px;
  padding: 1rem 1.1rem;
}

.review-card-header {
  display: flex;
  justify-content: space-between;
  gap: 1rem;
  align-items: start;
  margin-bottom: 0.5rem;
}

.review-card h4,
.review-card p {
  margin: 0;
}

.review-card h4 {
  color: #15324b;
  font-size: 1.05rem;
  margin-bottom: 0.25rem;
}

.review-author {
  color: #58708a;
  font-size: 0.95rem;
}

.review-card-stars {
  color: #f4b942;
  letter-spacing: 0.1rem;
  white-space: nowrap;
}

.review-card-comment {
  color: #34495e;
  line-height: 1.6;
}

.empty-state {
  color: #58708a;
  background: white;
  border: 1px dashed #c5d6e8;
  border-radius: 14px;
  padding: 1.1rem;
  text-align: center;
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

  .reviews-header,
  .review-list-header {
    flex-direction: column;
    align-items: stretch;
  }

  .reviews-grid {
    grid-template-columns: 1fr;
  }

  .review-summary {
    min-width: 0;
  }
}
</style>

<script type="module">
import { initializeApp } from "https://www.gstatic.com/firebasejs/10.8.0/firebase-app.js";
import {
  addDoc,
  collection,
  getDocs,
  getFirestore,
  limit,
  orderBy,
  query,
  serverTimestamp
} from "https://www.gstatic.com/firebasejs/10.8.0/firebase-firestore.js";

(() => {
  const firebaseConfig = {
    apiKey: "AIzaSyAM6U2dy7EKF0ey1TO_YV_WmLZ7YbRUdO4",
    authDomain: "journeyhue.firebaseapp.com",
    projectId: "journeyhue",
    storageBucket: "journeyhue.firebasestorage.app",
    messagingSenderId: "551447445192",
    appId: "1:551447445192:web:31a99fc5bc3914be5a6ffd",
    measurementId: "G-PXY3M7PTNB"
  };

  const app = initializeApp(firebaseConfig);
  const db = getFirestore(app);
  const reviewsCollection = collection(db, "book_reviews_lucid_dreaming");

  const form = document.getElementById("review-form");
  const reviewsList = document.getElementById("reviews-list");
  const feedback = document.getElementById("review-feedback");
  const averageRating = document.getElementById("average-rating");
  const averageRatingStars = document.getElementById("average-rating-stars");
  const reviewCount = document.getElementById("review-count");
  const refreshReviewsButton = document.getElementById("refresh-reviews");

  if (!form || !reviewsList || !feedback || !averageRating || !averageRatingStars || !reviewCount || !refreshReviewsButton) {
    return;
  }

  const starString = (rating) => {
    const rounded = Math.round(rating);
    return "★".repeat(rounded) + "☆".repeat(5 - rounded);
  };

  const escapeHtml = (value) =>
    value
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/\"/g, "&quot;")
      .replace(/'/g, "&#39;");

  const renderSummary = (reviews) => {
    if (!reviews.length) {
      averageRating.textContent = "0.0";
      averageRatingStars.textContent = "☆☆☆☆☆";
      reviewCount.textContent = "0";
      return;
    }

    const average = reviews.reduce((sum, review) => sum + Number(review.rating), 0) / reviews.length;
    averageRating.textContent = average.toFixed(1);
    averageRatingStars.textContent = starString(average);
    reviewCount.textContent = String(reviews.length);
  };

  const renderReviews = (reviews) => {
    renderSummary(reviews);

    if (!reviews.length) {
      reviewsList.innerHTML = '<div class="empty-state">No reviews yet. Be the first to share your thoughts.</div>';
      return;
    }

    reviewsList.innerHTML = reviews
      .map((review) => {
        const date = new Date(review.createdAt);
        const formattedDate = Number.isNaN(date.getTime())
          ? "Recently"
          : date.toLocaleDateString(undefined, { year: "numeric", month: "short", day: "numeric" });

        return `
          <article class="review-card">
            <div class="review-card-header">
              <div>
                <h4>${escapeHtml(review.title)}</h4>
                <p class="review-author">${escapeHtml(review.name)} • ${formattedDate}</p>
              </div>
              <div class="review-card-stars" aria-label="${review.rating} out of 5 stars">${starString(Number(review.rating))}</div>
            </div>
            <p class="review-card-comment">${escapeHtml(review.comment)}</p>
          </article>
        `;
      })
      .join("");
  };

  const setFeedback = (message, isError = false) => {
    feedback.textContent = message;
    feedback.style.color = isError ? "#b04a4a" : "#58708a";
  };

  const loadReviews = async () => {
    reviewsList.innerHTML = '<div class="empty-state">Loading reviews...</div>';

    try {
      const reviewsQuery = query(reviewsCollection, orderBy("createdAt", "desc"), limit(50));
      const snapshot = await getDocs(reviewsQuery);
      const reviews = snapshot.docs.map((doc) => {
        const data = doc.data();
        return {
          name: String(data.name || "Anonymous"),
          title: String(data.title || "Untitled review"),
          comment: String(data.comment || ""),
          rating: Number(data.rating || 0),
          createdAt: data.createdAt && typeof data.createdAt.toDate === "function"
            ? data.createdAt.toDate().toISOString()
            : new Date().toISOString()
        };
      });

      renderReviews(reviews);
    } catch (error) {
      console.error("Error loading reviews:", error);
      reviewsList.innerHTML = '<div class="empty-state">Reviews are unavailable right now. Check your Firebase Firestore rules and try again.</div>';
      renderSummary([]);
    }
  };

  form.addEventListener("submit", async (event) => {
    event.preventDefault();

    const formData = new FormData(form);
    const name = String(formData.get("name") || "").trim();
    const title = String(formData.get("title") || "").trim();
    const comment = String(formData.get("comment") || "").trim();
    const rating = Number(formData.get("rating"));

    if (!name || !title || !comment || !rating) {
      setFeedback("Please complete your name, rating, headline, and comment.", true);
      return;
    }

    const submitButton = form.querySelector('button[type="submit"]');
    if (submitButton) {
      submitButton.disabled = true;
      submitButton.textContent = "Posting...";
    }

    try {
      await addDoc(reviewsCollection, {
        bookSlug: "lucid-dreaming",
        name,
        title,
        comment,
        rating,
        createdAt: serverTimestamp()
      });

      form.reset();
      setFeedback("Your review is now live for everyone.");
      await loadReviews();
    } catch (error) {
      console.error("Error saving review:", error);
      setFeedback("Could not post your review. Make sure Firestore is enabled and your rules allow writes.", true);
    } finally {
      if (submitButton) {
        submitButton.disabled = false;
        submitButton.textContent = "Post Review";
      }
    }
  });

  refreshReviewsButton.addEventListener("click", () => {
    setFeedback("Refreshing reviews...");
    loadReviews().then(() => {
      setFeedback("Reviews refreshed.");
    });
  });

  loadReviews();
})();
</script>
