# Everyday Data

> **The data behind everyday decisions.**

[![Live Site](https://img.shields.io/badge/Live%20Site-Everyday%20Data-0F766E?style=for-the-badge)](https://happykarhu.github.io/everyday-data/)

Welcome to **Everyday Data**.

Everyday Data is an independent research project that explores everyday questions using public data, scientific literature, transparent calculations, and clear visualizations.

> **Can one person's everyday choices really make a measurable difference?**

The goal is simple: to transform complex data into practical insights that anyone can understand and use in everyday life.

## What you'll find here

Each project follows the same research process:

1. Define a real-world question.
2. Collect data from official and scientific sources.
3. Document assumptions and references.
4. Analyze the data using Python (Pandas).
5. Visualize the results with Power BI.
6. Explain the findings in a clear and accessible way.

## Topics

Current and future research may include:

- 💧 Water conservation
- ⚡ Energy use
- 🌍 Environmental impact
- 🏠 Everyday habits
- 🍎 Health and lifestyle
- 📊 Public statistics

## Repository Structure

The repository is built with **Hugo**. The project layouts, custom styling, and site structure are defined in the `layouts/` and `assets/` directories, while `content/` holds all written articles and project bundles.

```text
everyday-data/
├── assets/
│   └── css/
│       └── main.css       # Custom styling
├── content/
│   ├── _index.md          # Homepage content/metadata
│   ├── about.md           # About Everyday Data
│   └── research/
│       ├── _index.md      # Research section metadata
│       └── projects/ and other articles-researches
│           ├── # Project article 1
│           ├── # Project article 2
│           └── # Project article 3 ...
├── layouts/
│   ├── index.html         # Homepage layout template
│   ├── partials
│       ├── footer.html
│       └── header.html
│   └── _default/
│       ├── baseof.html    # Main HTML structure
│       └── single.html    # Default single page layout
├── static/
│   ├── images
│       ├── background.svg
│       ├── mojca-about.jpg
│       └── logo.png
├── hugo.toml              # Hugo site configuration
├── AGENTS.md              # Guidelines & context for AI assistants
└── README.md              # Project documentation
```

## Website structure

```
Home
├── Featured Research
├── Latest Research
├── Why Everyday Data?
└── Explore all research

Research
├── Environment
├── Health
├── Everyday Habits
├── Public Statistics
└── All projects

About
├── Why Everyday Data?
├── Research methodology
├── Tools
└── Contact
```

## Technology

The website is built with **Hugo** and hosted on **GitHub Pages**.

Research and visualizations are created using:

- Python
- Pandas
- Power BI
- Git & GitHub
- Markdown
- HTML & CSS

Interactive poll data is stored anonymously using **Supabase**.

## 🌐 Website 

Visit the project:

👉 https://happykarhu.github.io/everyday-data/

## Project status

Everyday Data is currently a work in progress.

The website and research projects are being developed step by step. Articles may be published and shared while the project continues to grow, with new research, visualizations, and improvements added over time.

Feedback & Suggestions

I’m always happy to hear your thoughts.

If you have a suggestion, notice something that could be improved, or have an idea for a future article or visualization, feel free to share it.

Everyday Data is also part of my learning journey in data analysis and web development, so feedback and new perspectives are very welcome.

## Research Principles

Every research project aims to be:

- Evidence-based
- Transparent
- Reproducible
- Easy to understand
- Built from publicly available data whenever possible


## Purpose & About the author

This repository also documents my journey in data analysis and web development while building practical, evidence-based research projects that anyone can verify, reproduce, and learn from.

---

*"Good decisions start with good data."*