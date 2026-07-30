# Everyday Data

> **The data behind everyday decisions.**

Welcome to **Everyday Data**.

Everyday Data is a collection of evidence-based research projects exploring everyday questions through official data, scientific research, transparent calculations, and clear visualizations.

> **Can one person's everyday choices really make a measurable difference?**

This project investigates common questions using reliable evidence instead of assumptions. The goal is to transform data into clear, practical, and understandable insights.

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
│       └── turning-off-the-tap/
│           ├── index.md   # Project article
│           ├── cover.jpg
│           └── graph1.png
├── layouts/
│   ├── index.html         # Homepage layout template
│   └── _default/
│       ├── baseof.html    # Main HTML structure
│       └── single.html    # Default single page layout
├── hugo.toml              # Hugo site configuration
├── AGENTS.md              # Guidelines & context for AI assistants
└── README.md              # Project documentation
```

Website structure

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

## Tools

- Hugo(Static Site Generator)
- Python
- Pandas
- Power BI
- Git & GitHub
- Excel
- Markdown

## First Project

**What is the environmental impact of turning off the tap while brushing your teeth for one year?**

*Status: In progress*

## Research Principles

Every research project aims to be:

- Evidence-based
- Transparent
- Reproducible
- Easy to understand
- Built from publicly available data whenever possible

## Purpose

This repository documents my journey in data analysis while building practical, evidence-based research projects that anyone can understand, verify, and reproduce.

---

*"Good decisions start with good data."*