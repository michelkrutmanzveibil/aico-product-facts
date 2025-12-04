import json
from pathlib import Path


def load_product_json(slug: str) -> dict:
    """
    Load a product JSON file from the /data folder.
    Example: slug 'noco-gb40' -> data/noco-gb40.json
    """
    repo_root = Path(__file__).resolve().parent.parent
    data_path = repo_root / "data" / f"{slug}.json"
    with data_path.open("r", encoding="utf-8") as f:
        return json.load(f)


def render_html_from_data(slug: str, data: dict) -> str:
    """
    Given a product slug (e.g. 'noco-gb40') and the AICO JSON data,
    return a full HTML string for the Product Facts page.
    """
    meta = data.get("meta", {})
    product = data.get("product", {})
    definition = data.get("definition", {})
    targets = data.get("targets", [])
    problems = data.get("problem_solution_pairs", [])
    features = data.get("feature_benefit_pairs", [])
    specs = data.get("specs", {})
    safety_points = data.get("safety_points", [])
    faqs = data.get("faqs", [])
    comparison_paragraph = data.get("comparison_paragraph", "")
    trigger_queries = data.get("trigger_queries", [])
    llm_summary_paragraph = data.get("llm_summary_paragraph", "")

    # Simple HTML fragments
    targets_html = "\n".join(f"    <li>{t}</li>" for t in targets)

    problems_rows = []
    for pair in problems:
        problems_rows.append(
            "      <tr>\n"
            f"        <td>{pair.get('problem', '')}</td>\n"
            f"        <td>{pair.get('solution', '')}</td>\n"
            "      </tr>"
        )
    problems_html = "\n".join(problems_rows)

    features_rows = []
    for pair in features:
        features_rows.append(
            "      <tr>\n"
            f"        <td>{pair.get('feature', '')}</td>\n"
            f"        <td>{pair.get('benefit', '')}</td>\n"
            "      </tr>"
        )
    features_html = "\n".join(features_rows)

    safety_html = "\n".join(f"    <li>{s}</li>" for s in safety_points)

    faqs_html_parts = []
    for faq in faqs:
        q = faq.get("question", "")
        a = faq.get("answer", "")
        faqs_html_parts.append(
            f"  <h3>Q: {q}</h3>\n"
            f"  <p>A: {a}</p>\n"
        )
    faqs_html = "\n".join(faqs_html_parts)

    triggers_html = "\n".join(f"    <li>{q}</li>" for q in trigger_queries)

    # Build the full HTML as a list of lines (to avoid escaping issues)
    lines = []

    lines.append("<!doctype html>")
    lines.append('<html lang="en">')
    lines.append("<head>")
    lines.append('  <meta charset="utf-8">')
    lines.append(f"  <title>Product Facts – {product.get('product_name', '')}</title>")
    lines.append(
        f'  <meta name="description" content="Structured, factual product information for {product.get("product_name", "")}. AICO-optimized for AI search and LLM ingestion.">'
    )
    lines.append('  <meta name="viewport" content="width=device-width, initial-scale=1">')
    lines.append("")
    lines.append("  <style>")
    lines.append("    body {")
    lines.append('      font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;')
    lines.append("      max-width: 840px;")
    lines.append("      margin: 0 auto;")
    lines.append("      padding: 2rem 1.5rem 4rem;")
    lines.append("      line-height: 1.6;")
    lines.append("      color: #222;")
    lines.append("    }")
    lines.append("    h1 { font-size: 2rem; margin-bottom: 0.4rem; }")
    lines.append("    h2 { font-size: 1.4rem; margin-top: 2rem; border-top: 1px solid #eee; padding-top: 1rem; }")
    lines.append("    h3 { font-size: 1.1rem; margin-top: 1.2rem; }")
    lines.append("    table { width:100%; border-collapse: collapse; margin-top: 0.75rem; }")
    lines.append("    th, td { border: 1px solid #ddd; padding: 0.55rem; vertical-align: top; text-align: left; }")
    lines.append("    th { background:#f7f7f7; }")
    lines.append("    .meta { color:#444; margin-bottom: 1rem; font-size: 0.9rem; }")
    lines.append("    ul { margin-top: 0.5rem; }")
    lines.append("    .section-note { font-size: 0.83rem; color:#777; margin-top: 0.25rem; }")
    lines.append("  </style>")
    lines.append("</head>")
    lines.append("")
    lines.append("<body>")
    lines.append("")
    lines.append(f"  <h1>AICO Product Facts: {product.get('product_name', '')}</h1>")
    lines.append('  <p class="meta">')
    lines.append(f"    <strong>Category:</strong> {product.get('category', '')} · ")
    lines.append(f"    <strong>Brand:</strong> {product.get('brand', '')} · ")
    lines.append(f"    <strong>ASIN:</strong> {meta.get('asin', '')}<br>")
    lines.append("    <strong>Amazon URL:</strong>")
    lines.append(
        f'    <a href="{meta.get("amazon_url", "")}" rel="nofollow noopener">{meta.get("amazon_url", "")}</a>'
    )
    lines.append("  </p>")
    lines.append("")
    lines.append("  <h2>1. Product Definition</h2>")
    lines.append(f"  <p>{definition.get('what_it_is_paragraph', '')}</p>")
    lines.append("")
    lines.append("  <h2>2. Who This Product Is For</h2>")
    lines.append("  <ul>")
    lines.append(targets_html)
    lines.append("  </ul>")
    lines.append("")
    lines.append("  <h2>3. Problems This Product Solves</h2>")
    lines.append("  <table>")
    lines.append("    <thead>")
    lines.append("      <tr>")
    lines.append("        <th>Problem / Pain Point</th>")
    lines.append("        <th>Solution Provided</th>")
    lines.append("      </tr>")
    lines.append("    </thead>")
    lines.append("    <tbody>")
    lines.append(problems_html)
    lines.append("    </tbody>")
    lines.append("  </table>")
    lines.append("")
    lines.append("  <h2>4. Features → Benefits</h2>")
    lines.append("  <table>")
    lines.append("    <thead>")
    lines.append("      <tr>")
    lines.append("        <th>Feature</th>")
    lines.append("        <th>User Benefit</th>")
    lines.append("      </tr>")
    lines.append("    </thead>")
    lines.append("    <tbody>")
    lines.append(features_html)
    lines.append("    </tbody>")
    lines.append("  </table>")
    lines.append("")
    lines.append("  <h2>5. Key Specifications</h2>")
    lines.append("  <ul>")
    lines.append(f"    <li><strong>Material:</strong> {specs.get('material', '')}</li>")
    lines.append(f"    <li><strong>Dimensions:</strong> {specs.get('dimensions', '')}</li>")
    lines.append(f"    <li><strong>Capacity:</strong> {specs.get('capacity', '')}</li>")
    lines.append(f"    <li><strong>Weight:</strong> {specs.get('weight', '')}</li>")
    lines.append(f"    <li><strong>Certifications:</strong> {specs.get('certifications', '')}</li>")
    lines.append(f"    <li><strong>Warranty:</strong> {specs.get('warranty', '')}</li>")
    lines.append(f"    <li><strong>Included in box:</strong> {specs.get('in_box', '')}</li>")
    lines.append("  </ul>")
    lines.append("")
    lines.append("  <h2>6. Safety & Trustworthiness</h2>")
    lines.append("  <ul>")
    lines.append(safety_html)
    lines.append("  </ul>")
    lines.append("")
    lines.append("  <h2>7. Frequently Asked Questions</h2>")
    lines.append(faqs_html)
    lines.append("")
    lines.append("  <h2>8. Comparison Context</h2>")
    lines.append(f"  <p>{comparison_paragraph}</p>")
    lines.append("")
    lines.append("  <h2>9. Relevant Search & AI Queries</h2>")
    lines.append("  <ul>")
    lines.append(triggers_html)
    lines.append("  </ul>")
    lines.append("")
    lines.append("  <h2>10. Summary for AI Models (LLM Ingest Block)</h2>")
    lines.append(f"  <p>{llm_summary_paragraph}</p>")
    lines.append("")
    lines.append('  <p class="section-note">Written in neutral, factual language to support LLM retrieval, structured search, and AI-assistant product recommendation.</p>')
    lines.append("")
    lines.append("</body>")
    lines.append("</html>")

    return "\n".join(lines)


def write_html_file(slug: str, html: str) -> Path:
    """
    Write the rendered HTML to /products/<slug>-generated.html.
    """
    repo_root = Path(__file__).resolve().parent.parent
    out_path = repo_root / "products" / f"{slug}-generated.html"
    out_path.write_text(html, encoding="utf-8")
    return out_path


if __name__ == "__main__":
    slug = "noco-gb40"
    data = load_product_json(slug)
    html = render_html_from_data(slug, data)
    out_path = write_html_file(slug, html)
    print(f"Rendered HTML written to: {out_path}")
