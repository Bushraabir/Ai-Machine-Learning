---
title: Home
description: A first-principles AI/ML learning journal by Bushra Abir
hide:
  - navigation
  - toc
---

<style>
/* ── Custom homepage styles ───────────────────────── */
:root {
  --primary-hue: 265;
  --accent-hue: 185;
}

.md-content__inner {
  max-width: 900px;
  margin: 0 auto;
  padding: 0 1rem;
}

/* Hero */
.hero {
  padding: 5rem 0 3rem;
  text-align: left;
  position: relative;
}

.hero-eyebrow {
  font-family: "JetBrains Mono", monospace;
  font-size: 0.78rem;
  letter-spacing: 0.18em;
  text-transform: uppercase;
  color: var(--md-accent-fg-color);
  margin-bottom: 1.2rem;
  opacity: 0.85;
}

.hero-title {
  font-size: clamp(2.4rem, 5vw, 3.8rem);
  font-weight: 800;
  line-height: 1.12;
  letter-spacing: -0.03em;
  margin: 0 0 1.4rem;
  color: var(--md-default-fg-color);
}

.hero-title em {
  font-style: normal;
  color: var(--md-accent-fg-color);
}

.hero-subtitle {
  font-size: 1.05rem;
  line-height: 1.75;
  color: var(--md-default-fg-color--light);
  max-width: 600px;
  margin-bottom: 2.5rem;
}

/* Manifesto quote */
.manifesto {
  border-left: 3px solid var(--md-accent-fg-color);
  padding: 1rem 0 1rem 1.5rem;
  margin: 3rem 0;
  font-family: "JetBrains Mono", monospace;
  font-size: 0.88rem;
  line-height: 1.7;
  color: var(--md-default-fg-color--light);
  background: var(--md-code-bg-color);
  border-radius: 0 6px 6px 0;
}

.manifesto strong {
  color: var(--md-accent-fg-color);
  font-weight: 600;
}

/* Card grid */
.card-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(260px, 1fr));
  gap: 1.2rem;
  margin: 2.5rem 0;
}

.card {
  border: 1px solid var(--md-default-fg-color--lightest);
  border-radius: 10px;
  padding: 1.4rem 1.5rem;
  text-decoration: none !important;
  display: block;
  transition: border-color 0.18s ease, transform 0.18s ease, box-shadow 0.18s ease;
  background: var(--md-default-bg-color);
  position: relative;
  overflow: hidden;
}

.card::before {
  content: '';
  position: absolute;
  top: 0; left: 0; right: 0;
  height: 3px;
  background: var(--card-accent, var(--md-accent-fg-color));
  transform: scaleX(0);
  transform-origin: left;
  transition: transform 0.22s ease;
}

.card:hover {
  border-color: var(--md-accent-fg-color);
  transform: translateY(-3px);
  box-shadow: 0 8px 24px rgba(0,0,0,0.12);
  text-decoration: none !important;
}

.card:hover::before {
  transform: scaleX(1);
}

.card-icon {
  font-size: 1.6rem;
  margin-bottom: 0.7rem;
  display: block;
}

.card-title {
  font-size: 1rem;
  font-weight: 700;
  color: var(--md-default-fg-color);
  margin: 0 0 0.4rem;
  letter-spacing: -0.01em;
}

.card-desc {
  font-size: 0.82rem;
  color: var(--md-default-fg-color--light);
  line-height: 1.55;
  margin: 0;
}

/* Progress table */
.progress-section {
  margin: 3.5rem 0;
}

.progress-section h2 {
  font-size: 1.1rem;
  font-weight: 700;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--md-default-fg-color--light);
  margin-bottom: 1.2rem;
  padding-bottom: 0.5rem;
  border-bottom: 1px solid var(--md-default-fg-color--lightest);
}

.status-table {
  width: 100%;
  border-collapse: collapse;
  font-size: 0.88rem;
}

.status-table th {
  text-align: left;
  font-family: "JetBrains Mono", monospace;
  font-size: 0.72rem;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: var(--md-default-fg-color--lighter);
  padding: 0.5rem 1rem 0.5rem 0;
  border-bottom: 1px solid var(--md-default-fg-color--lightest);
}

.status-table td {
  padding: 0.7rem 1rem 0.7rem 0;
  border-bottom: 1px solid var(--md-default-fg-color--lightest);
  vertical-align: middle;
  color: var(--md-default-fg-color);
}

.badge {
  display: inline-block;
  font-family: "JetBrains Mono", monospace;
  font-size: 0.7rem;
  padding: 0.2rem 0.6rem;
  border-radius: 20px;
  letter-spacing: 0.06em;
  font-weight: 600;
}

.badge-active   { background: rgba(16,185,129,0.15); color: #10b981; }
.badge-next     { background: rgba(139,92,246,0.15); color: #8b5cf6; }
.badge-planned  { background: rgba(107,114,128,0.15); color: var(--md-default-fg-color--light); }
.badge-done     { background: rgba(6,182,212,0.15);  color: #06b6d4; }

/* Principle block */
.principles {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
  gap: 1rem;
  margin: 2rem 0;
}

.principle {
  padding: 1.2rem;
  border-radius: 8px;
  background: var(--md-code-bg-color);
  font-size: 0.85rem;
}

.principle-num {
  font-family: "JetBrains Mono", monospace;
  font-size: 1.4rem;
  font-weight: 800;
  color: var(--md-accent-fg-color);
  opacity: 0.5;
  display: block;
  margin-bottom: 0.3rem;
}

.principle-text {
  line-height: 1.5;
  color: var(--md-default-fg-color);
}

/* Closing */
.closing {
  margin: 4rem 0 2rem;
  padding: 2rem;
  border-radius: 10px;
  background: var(--md-code-bg-color);
  font-family: "JetBrains Mono", monospace;
  font-size: 0.82rem;
  line-height: 1.9;
  color: var(--md-default-fg-color--light);
  text-align: center;
}
</style>

<div class="hero">
  <div class="hero-eyebrow">learning journal · ai & machine learning</div>
  <h1 class="hero-title">
    First principles.<br>
    No hand-waving.<br>
    <em>Actually learned.</em>
  </h1>
  <p class="hero-subtitle">
    A rigorous notebook built around one rule: if I can't derive it, implement it from scratch, and explain it clearly — I don't know it yet. Everything here has been earned, not consumed.
  </p>
</div>

<div class="manifesto">
<strong>The deal I made with myself:</strong><br>
Read the note → Derive the key equations by hand → Implement from scratch<br>
→ Verify against sklearn/PyTorch → Only then move on.<br><br>
The version of me that gets where I'm trying to go is just the current version, kept going.
</div>

---

## ✦ The Map

```mermaid
graph LR
    A[📐 Mathematics] --> D[🤖 ML Algorithms]
    B[🐍 Programming] --> D
    C[🌲 DSA] --> D
    D --> E[🧠 Neural Networks & Deep Learning]
    E --> F[🔬 Projects]
    F --> G[📄 Research]
    G --> F
```

The loop at the end is intentional. Projects surface gaps. Research fills them. Repeat.

---

## ✦ Start Here

<div class="card-grid">

  <a class="card" href="01.Maths/00.Maths/" style="--card-accent: #f59e0b;">
    <span class="card-icon">📐</span>
    <p class="card-title">Mathematics</p>
    <p class="card-desc">Linear algebra, calculus, probability, statistics. The substrate everything else is built on.</p>
  </a>

  <a class="card" href="02.Python/00.Python/" style="--card-accent: #3b82f6;">
    <span class="card-icon">🐍</span>
    <p class="card-title">Programming</p>
    <p class="card-desc">Python from first principles through NumPy, vectorized thinking, and clean ML code.</p>
  </a>

  <a class="card" href="03.Data Structure and Algorithms/" style="--card-accent: #10b981;">
    <span class="card-icon">🌲</span>
    <p class="card-title">Data Structures & Algorithms</p>
    <p class="card-desc">Core structures, graph algorithms, dynamic programming. The problem-solving muscle.</p>
  </a>

  <a class="card" href="04.ML/00.Machine Learning/" style="--card-accent: #8b5cf6;">
    <span class="card-icon">🤖</span>
    <p class="card-title">Machine Learning</p>
    <p class="card-desc">Supervised, unsupervised, ensembles, probabilistic models — all derived, not just used.</p>
  </a>

  <a class="card" href="05.Neural Networks & Deep Learning/" style="--card-accent: #ec4899;">
    <span class="card-icon">🧠</span>
    <p class="card-title">Deep Learning</p>
    <p class="card-desc">Backprop from scratch. CNNs, RNNs, Transformers, diffusion. Autograd comes last.</p>
  </a>

  <a class="card" href="06.Projects/" style="--card-accent: #06b6d4;">
    <span class="card-icon">🔬</span>
    <p class="card-title">Projects</p>
    <p class="card-desc">No tutorial projects. Real problems, paper reproductions, and things I actually care about.</p>
  </a>

</div>

---

<div class="progress-section">
<h2>Current Progress</h2>

<table class="status-table">
  <thead>
    <tr>
      <th>Area</th>
      <th>Focus</th>
      <th>Status</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Python Fundamentals</strong></td>
      <td>Variables → OOP → Decorators → Pythonic patterns</td>
      <td><span class="badge badge-active">active</span></td>
    </tr>
    <tr>
      <td><strong>Linear Algebra</strong></td>
      <td>MIT 18.06 — got the intuition, building the depth</td>
      <td><span class="badge badge-active">active</span></td>
    </tr>
    <tr>
      <td><strong>Probability</strong></td>
      <td>Harvard Stat 110 — distributions, Bayes, MLE</td>
      <td><span class="badge badge-active">active</span></td>
    </tr>
    <tr>
      <td><strong>Supervised ML</strong></td>
      <td>Linear/Logistic regression, SVMs — deriving by hand</td>
      <td><span class="badge badge-active">active</span></td>
    </tr>
    <tr>
      <td><strong>Unsupervised ML</strong></td>
      <td>K-Means, PCA, DBSCAN, GMM/EM</td>
      <td><span class="badge badge-next">up next</span></td>
    </tr>
    <tr>
      <td><strong>Ensemble Methods</strong></td>
      <td>Random Forests, Gradient Boosting, XGBoost</td>
      <td><span class="badge badge-planned">planned</span></td>
    </tr>
    <tr>
      <td><strong>Backpropagation</strong></td>
      <td>Implement from scratch in NumPy before touching autograd</td>
      <td><span class="badge badge-planned">planned</span></td>
    </tr>
    <tr>
      <td><strong>Transformers</strong></td>
      <td>Attention from scratch — not just "here's the architecture"</td>
      <td><span class="badge badge-planned">planned</span></td>
    </tr>
    <tr>
      <td><strong>Linear Regression (scratch)</strong></td>
      <td>Normal equation, geometry of loss surfaces</td>
      <td><span class="badge badge-done">done</span></td>
    </tr>
  </tbody>
</table>

</div>

---

## ✦ How This Notebook Works

<div class="principles">
  <div class="principle">
    <span class="principle-num">01</span>
    <span class="principle-text">Derive first. Every key result gets worked out by hand before being used.</span>
  </div>
  <div class="principle">
    <span class="principle-num">02</span>
    <span class="principle-text">Implement from scratch. NumPy before sklearn. sklearn before PyTorch.</span>
  </div>
  <div class="principle">
    <span class="principle-num">03</span>
    <span class="principle-text">Know the prerequisites. If something feels like magic, there's a skipped step.</span>
  </div>
  <div class="principle">
    <span class="principle-num">04</span>
    <span class="principle-text">Exit criteria per note. Don't move forward until you can clear it cold.</span>
  </div>
</div>

---

## ✦ The Reading Stack

These are the eleven books and six courses this vault is built around:

=== "Books"

    | Book | Domain | When |
    |------|--------|------|
    | Programming: Principles & Practice (C++) | Systems | Phase 1 |
    | Discrete Mathematics & Its Applications | Foundations | Phase 1 |
    | Introduction to Linear Algebra (Strang) | Maths | Phase 1 |
    | Introduction to Algorithms (CLRS) | DSA | Phase 1–2 |
    | Introduction to Probability | Maths | Phase 1–2 |
    | Computer Systems: A Programmer's Perspective | Systems | Phase 2 |
    | Operating System Concepts | Systems | Phase 2 |
    | Database System Concepts | Systems | Phase 2 |
    | Artificial Intelligence: A Modern Approach | AI | Phase 2–3 |
    | Pattern Recognition and Machine Learning | ML | Phase 3 |
    | Deep Learning (Goodfellow) | DL | Phase 3 |

=== "Courses"

    | Course | Institution | Synergises With |
    |--------|-------------|-----------------|
    | Stat 110 | Harvard | PRML, probability notes |
    | Linear Algebra 18.06 | MIT | PCA, NNs, all of ML |
    | Statistics 18.650 | MIT | ML evaluation, inference |
    | Multivariable Calculus 18.02 | MIT | Backprop, optimisation |
    | Machine Learning CS229 | Stanford | Entire ML section |
    | CNNs CS231n | Stanford | Deep learning section |

---

<div class="closing">
This is going to take longer than I want it to.<br>
There will be weeks where nothing clicks and the material feels impenetrable.<br>
That's part of it.<br><br>
<strong>The version of me that gets there is just the current version, kept going.</strong>
</div>