# Everyday Data

Everyday Data is an independent research project that explores everyday questions through public data, scientific literature, transparent calculations, and clear visual communication.

The website is built with **Hugo** and published on **GitHub Pages**.

The primary goal is to produce research articles that are accurate, understandable, reproducible, and useful for everyday readers.

Every article should explain not only the results, but also how those results were obtained.

---

## Core principles

- Prioritize clarity over complexity.
- Use evidence-based reasoning.
- Explain how conclusions were reached, not only the final result.
- Keep calculations and assumptions transparent.
- Avoid sensationalism or exaggerated claims.
- Write for a general audience, not only for researchers.

---

## Project principles

- Keep the design clean, modern, and approachable.
- Prioritize readability and accessibility.
- Support light mode first while avoiding harsh white backgrounds.
- Create an experience that feels comfortable during both daytime and evening use.
- Use reusable, maintainable, and well-organized code.
- Favor clarity over unnecessary visual effects.
- Keep the user interface simple and intuitive.
- Prioritize content over decoration.
- Keep pages fast, lightweight, and easy to maintain.

---

## Website structure

```text
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

Images should remain inside the relevant project folder whenever possible.

---

## Design principles

The visual identity should communicate trust, curiosity, and optimism.

- Keep the interface clean and lightweight.
- Favor readability and accessibility.
- Use generous whitespace and rounded components.
- Avoid harsh white backgrounds and excessive visual effects.
- Ensure the design supports the content rather than competing with it.

### Brand colors

- Emerald: `#0F766E`
- Amber: `#F59E0B`
- Background: `#E5E0D6`
- Card background: `#F7F5F0`

Do not introduce a new color palette unless explicitly requested.

---

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

---

## Research workflow

Each article should:

1. Start with a real-world question.
2. Explain why the topic matters.
3. Describe the data sources and methodology.
4. Document assumptions transparently.
5. Show calculations clearly.
6. Analyze data using Python when appropriate.
7. Include charts where they improve understanding.
8. Discuss limitations and uncertainty.
9. Cite reliable sources whenever possible.
10. End with practical takeaways.

Write in a calm, neutral, evidence-based tone.

---

## Project structure

- `content/` – pages and research articles
- `projects/` – research projects
- `library/` – research source library
- `assets/` – CSS, fonts, and theme assets
- `layouts/` – Hugo templates
- `static/` – images, icons, logos, and downloadable files
- `data/` – structured data used by Hugo

---

## Coding guidelines

When generating code:

- Prefer reusable solutions.
- Avoid duplication.
- Keep CSS modular.
- Keep HTML semantic.
- Prioritize readability.
- Document non-obvious code.
- Avoid unnecessary JavaScript.
- Preserve the existing project structure.
- Extend existing components instead of replacing them whenever possible.

---

## Design consistency

Do not redesign the website unless explicitly requested.

When suggesting code:

- Preserve the existing color palette.
- Preserve spacing and typography.
- Preserve component naming.
- Reuse existing CSS variables.
- Extend existing layouts instead of replacing them.

Everyday Data should feel optimistic, trustworthy, and easy to understand.

The website is intended for everyone—not only researchers or data scientists.

Complex topics should be explained using clear language, transparent calculations, and simple visualizations.

---

## AI assistant guidelines

Before suggesting code or changes:

- Do not assume files, folders, layouts, templates, or components exist.
- Do not invent project structure.
- If you are unsure whether a file, folder, variable, or component exists, ask first.
- Prefer asking one clarifying question instead of making assumptions.
- Work with the existing project whenever possible.
- Modify existing code instead of rewriting large sections unless requested.
- Keep changes focused and minimal.
- Explain why a significant change is recommended.
- If information is missing, explicitly state what you need before generating code.