# AICO Engine – Input Format (Collector → Brain)

This file defines the **input format** that the AICO "collector" must produce
before sending anything to the LLM (the "brain").

The collector takes an Amazon product URL and returns a JSON object
with the **raw listing data**.

---

## 1. Input from the user

The user provides:

- `amazon_url` – the full URL to the product page on Amazon.

Example:

```json
{
  "amazon_url": "https://www.amazon.com/NOCO-GB40-UltraSafe-Lithium-Starter/dp/B015TKUPIC"
}
