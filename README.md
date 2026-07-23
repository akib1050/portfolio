# Ali Haider Talukder Akib — Portfolio

Personal portfolio website for **Ali Haider Talukder Akib**, Software Engineer II at Brain Station 23.

Built as a fast, dependency-free static site — plain HTML, CSS and JavaScript — so it deploys anywhere with zero build step.

## Features

- Responsive, mobile-first design
- Dark / light theme (remembered across visits)
- Animated hero with typed roles
- Animated stats counters and skill bars
- Filterable projects grid
- Experience timeline
- Competitive-programming achievements
- Working contact form (via FormSubmit)
- Downloadable resume

## Structure

```
.
├── index.html          # Markup / content
├── styles.css          # Styles & theming
├── script.js           # Interactivity
└── assets/
    ├── img/            # Images
    └── docs/           # Resume / CV PDFs
```

## Run locally

Any static server works. For example:

```bash
npx serve .
# or
python -m http.server 5173
```

Then open the printed URL.

## Deploy

This is a static site, so you can host it for free on:

- **Netlify** — drag-and-drop the folder or connect the repo
- **Vercel** — import the repo (framework preset: "Other")
- **GitHub Pages** — push to a repo and enable Pages on the default branch
- **Cloudflare Pages** — connect the repo

No build command is required; the output directory is the project root.

## Customize

- Content lives in `index.html`.
- Projects and skills are data-driven in `script.js` (`PROJECTS`, `SKILLS`).
- Colors and theme tokens are CSS variables at the top of `styles.css`.
- The contact form posts to FormSubmit; the first submission triggers an email
  confirmation to activate the endpoint.
