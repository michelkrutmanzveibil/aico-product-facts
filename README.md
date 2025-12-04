# AICO Product Facts – MVP

This repo is the **public output layer** of the AICO (AI Context Optimization) engine.

The goal:  
Turn an Amazon product listing into a **clean, factual, LLM-ready “Product Facts” page** that lives here on GitHub Pages and can be ingested by AI models.

---

## 🔹 How the MVP works (high level)

For each product we want to optimize:

1. **Create a JSON data file** with all of the AICO fields.  
   - Lives in: `data/<slug>.json`  
   - Example: `data/noco-gb40.json`

2. **Render that JSON into the HTML template** to create a Product Facts page.  
   - Template lives in: `products/_template.html`  
   - Output lives in: `products/<slug>.html`  
   - Example: `products/noco-gb40.html`

3. GitHub Pages serves the HTML pages publicly at:  
   `https://michelkrutmanzveibil.github.io/aico-product-facts/products/<slug>.html`

This is the **final, LLM-facing representation** of each product.

---

## 🔹 Files and folders

- `/README.md`  
  This file. Quick overview of how AICO Product Facts works.

- `/products/_template.html`  
  The **generic** Product Facts HTML template, with placeholders like `{{product_name}}`, `{{category}}`, etc.  
  In the future, the AICO engine will automatically fill this template using the JSON data.

- `/products/noco-gb40.html`  
  A concrete example of a Product Facts page for the NOCO Boost Plus GB40 1000A jump starter.

- `/data/noco-gb40.json`  
  The structured AICO data for the same NOCO product.  
  This JSON is what the engine will generate from the Amazon listing.

---

## 🔹 Future automation

The next step in the MVP will be to add a small script or service that:

1. Takes an Amazon URL and raw listing text.
2. Uses an LLM to generate a JSON object matching the AICO schema.
3. Fills `_template.html` with that JSON and writes a new file in `/products/`.
4. Commits the result back to this repo so the new page is live.

For now, the repo is set up so that:

- **Data** lives in `/data/`
- **Template** lives in `/products/_template.html`
- **Rendered pages** live in `/products/*.html`

This keeps the MVP simple and makes it easy to plug in automation later.
