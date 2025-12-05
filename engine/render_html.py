import json
import os

def render_product(json_path, html_path, template_path="../products/template.html"):

    with open(json_path, "r") as f:
        data = json.load(f)

    with open(template_path, "r") as f:
        template = f.read()

    # Extract fields
    title = data["product"]["title"]
    desc = data["product"]["description"]

    # Build feature/benefit HTML
    fb_html = ""
    for pair in data["feature_benefit_pairs"]:
        fb_html += f"<li><strong>{pair['feature']}:</strong> {pair['benefit']}</li>"

    # Problem/solution
    ps_html = ""
    for pair in data["problem_solution_pairs"]:
        ps_html += f"<li><em>{pair['problem']}</em> → {pair['solution']}</li>"

    # Specs block
    specs_block = json.dumps(data["specs"], indent=4)

    # FAQs
    faq_html = ""
    for q in data["faqs"]:
        faq_html += f"<li><strong>{q['question']}</strong><br>{q['answer']}</li>"

    # Summary
    summary = data["llm_summary_paragraph"]

    # Render final page
    output = template.replace("{{title}}", title)\
                     .replace("{{description}}", desc)\
                     .replace("{{feature_benefits}}", fb_html)\
                     .replace("{{problems_solutions}}", ps_html)\
                     .replace("{{specs}}", specs_block)\
                     .replace("{{faqs}}", faq_html)\
                     .replace("{{summary}}", summary)

    # Save
    with open(html_path, "w") as f:
        f.write(output)

    print("HTML page created →", html_path)
