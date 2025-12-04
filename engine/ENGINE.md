# AICO Engine (MVP)

This folder will contain the code that turns **raw Amazon listings** into:

1. Structured AICO JSON (in `/data/`), and
2. Rendered HTML Product Facts pages (in `/products/`).

For the MVP, the engine will eventually do:

1. **Input**
   - Receive an Amazon URL.
   - Receive raw listing text (title, bullets, description, etc.) or scrape it in a later version.

2. **Transform**
   - Send the raw content to an LLM with a fixed prompt.
   - Get back a JSON object that follows the AICO schema used in `/data/*.json`.

3. **Render**
   - Load the HTML template in `products/_template.html`.
   - Replace placeholders (like `{{product_name}}`, `{{category}}`, etc.) with values from the JSON.
   - Generate a new HTML file in `products/<slug>.html` (e.g., `products/noco-gb40.html`).

4. **Publish**
   - Commit the new HTML file to this repo so GitHub Pages makes it public at:
     `https://michelkrutmanzveibil.github.io/aico-product-facts/products/<slug>.html`.

For now, this folder is just a placeholder.  
The next step will be to add a small script (e.g., in Python or Node) that:

- Reads a JSON file from `/data/`,
- Reads the HTML template from `/products/_template.html`,
- Produces a rendered HTML file in `/products/`.

That script will be the first concrete version of the **AICO engine**.
