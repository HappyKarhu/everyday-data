# Everyday Data

Everyday Data is an independent research project that explores everyday questions using public data, scientific literature, and transparent analysis.

The goal is to transform complex information into clear, practical insights that anyone can understand and use in everyday life.
The website is built with Hugo.

Every article should explain not only the results, but also how those results were obtained.

## Project principles

- Keep the design clean, modern, and approachable.
- Prioritize readability and accessibility.
- Support light mode first while avoiding harsh white backgrounds.
- Create an experience that feels comfortable during both daytime and evening use.
- Use reusable, maintainable, and well-organized code.
- Use rounded components and a positive visual style.
- Favor clarity over unnecessary visual effects.
- Every design decision should support the content rather than distract from it.
- Keep the user interface simple and intuitive.
- Prioritize content over decoration.
- Keep pages fast, lightweight, and easy to maintain.

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
Research articles belong inside `content/research/`.

Images should remain inside the project folder whenever possible.

## Visual Identity

The visual style should communicate trust, curiosity, and optimism.

The interface should feel calm and comfortable, encouraging visitors to stay and explore rather than overwhelming them with visual intensity.

The primary brand color is Emerald, complemented by Amber accents inspired by the project logo.

Prefer soft, muted backgrounds instead of bright white to reduce eye strain, especially during evening reading.

Cards should remain slightly lighter than the page background to create gentle depth without relying on strong shadows.

Use whitespace generously, rounded corners, subtle borders, and restrained animations to keep the interface focused on the content.

The visual design should always support the research rather than compete with it.

Primary color:
Emerald (#0F766E)

Accent color:
Amber (#F59E0B)

Background:
Warm light gray (#E5E0D6)

Cards:
Warm off-white (#F7F5F0)

Avoid bright white backgrounds and high-contrast interfaces.


## Technology

- Hugo
- GitHub Pages
- Python
- Pandas
- Matplotlib
- Markdown
- Git
- HTML
- CSS

## Research methodology

Each project follows the same workflow:

1. Define a research question.
2. Collect data from official, scientific, and other reputable public sources.
3. Document assumptions transparently.
4. Analyze data using Python.
5. Create clear visualizations.
6. Publish reproducible results.
7. Cite all data sources whenever possible.

## Project structure

- `content/` – pages and research articles
- `projects/` – research projects 
- `library/` – research source library 
- `assets/` – CSS, fonts, and theme assets
- `layouts/` – Hugo templates
- `static/` – images, icons, logos, and downloadable files
- `data/` – structured data used by Hugo

## Coding Guidelines

When generating code:

- prefer reusable solutions
- avoid duplication
- keep CSS modular
- keep HTML semantic
- prioritize readability
- document non-obvious code
- avoid unnecessary JavaScript
- preserve the existing project structure

---

## Writing Guidelines

Research articles should:

- begin with a real-world question
- explain why the topic matters
- describe the methodology
- present transparent calculations
- include charts where appropriate
- discuss limitations
- conclude with practical takeaways

Avoid sensationalism or exaggerated claims.

Write in a calm, evidence-based tone.

# Design Consistency

Do not redesign the website unless explicitly requested.

When suggesting code:

- preserve the existing color palette
- preserve spacing and typography
- preserve component naming
- reuse existing CSS variables
- extend existing layouts instead of replacing them

## Design philosophy

Everyday Data should feel optimistic, trustworthy, and easy to understand.

The website is intended for everyone—not only researchers or data scientists. Complex topics should be explained with clear language, transparent calculations, and simple visualizations.

When suggesting code or layouts, prefer reusable, maintainable, and well-documented solutions that fit the existing project structure.