# AICO – Manual End-to-End Run (MVP)

This document explains how to go from:

> **Amazon product URL → AICO JSON → AICO Product Facts HTML page**

using the current MVP setup, *manually*.

Later, this will be automated. For now, this is the “playbook”.

---

## 1. Collect raw listing data from Amazon

1. Open the Amazon product page.
2. Copy the following pieces:
   - Product **title**
   - **Bullet points**
   - Main **description** (and/or A+ content text)
   - Any **technical details / specs** table
   - Optionally: 2–5 short **review snippets**

3. Build a JSON object in this format:

```json
{
  "amazon_url": "https://www.amazon.com/EXAMPLE/dp/ASIN123",
  "raw_listing": {
    "title": "Full product title from Amazon",
    "bullets": [
      "First bullet from listing",
      "Second bullet...",
      "Third bullet..."
    ],
    "description": "Main product description text copied from the page.",
    "technical_details": "Any specs table or technical details text.",
    "top_reviews": [
      "Short snippet from a top review.",
      "Short snippet from another review."
    ]
  }
}
