import json
from pathlib import Path

def load_product_json(slug: str) -> dict:
    """
    Load a product JSON file from the /data folder.
    Example slug: "noco-gb40" -> data/noco-gb40.json
    """
    data_path = Path(__file__).resolve().parent.parent / "data" / f"{slug}.json"
    with data_path.open("r", encoding="utf-8") as f:
        return json.load(f)

def pretty_print_product(data: dict) -> None:
    """
    Print a few key sections so we can confirm the structure is correct.
    """
    meta = data.get("meta", {})
    product = data.get("product", {})
    definition = data.get("definition", {})
    targets = data.get("targets", [])
    problems = data.get("problem_solution_pairs", [])
    features = data.get("feature_benefit_pairs", [])

    print("=== META ===")
    print(f"ASIN: {meta.get('asin')}")
    print(f"Amazon URL: {meta.get('amazon_url')}")
    print()

    print("=== PRODUCT ===")
    print(f"Name: {product.get('product_name')}")
    print(f"Category: {product.get('category')}")
    print(f"Brand: {product.get('brand')}")
    print()

    print("=== DEFINITION ===")
    print(definition.get("what_it_is_paragraph", ""))
    print()

    print("=== TARGETS (who it's for) ===")
    for t in targets:
        print(f"- {t}")
    print()

    print("=== PROBLEMS → SOLUTIONS (first 2) ===")
    for pair in problems[:2]:
        print(f"- Problem: {pair.get('problem')}")
        print(f"  Solution: {pair.get('solution')}")
        print()

    print("=== FEATURES → BENEFITS (first 2) ===")
    for pair in features[:2]:
        print(f"- Feature: {pair.get('feature')}")
        print(f"  Benefit: {pair.get('benefit')}")
        print()


if __name__ == "__main__":
    # For now, we hardcode the slug for the NOCO product
    slug = "noco-gb40"
    data = load_product_json(slug)
    pretty_print_product(data)
