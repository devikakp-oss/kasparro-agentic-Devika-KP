# Examples

This document provides examples of inputs and outputs for the Multi-Agent Product Content Generation System.

## Example 1: Vitamin C Serum

### Input
```json
{
  "name": "Vitamin C Serum",
  "concentration": "20%",
  "skin_types": "dry, oily, combination",
  "ingredients": "ascorbic acid, hyaluronic acid, vitamin E",
  "benefits": "brightens skin, reduces wrinkles",
  "usage_instructions": "Apply daily in the morning",
  "side_effects": "mild irritation",
  "price": 29.99
}
```

### Outputs

#### FAQ Page (`outputs/faq.json`)
```json
{
  "page_type": "faq",
  "product_name": "Vitamin C Serum",
  "faqs": [
    {
      "category": "General",
      "question": "What is the name of this product?",
      "answer": "The product is called Vitamin C Serum."
    },
    {
      "category": "Ingredients",
      "question": "What is the concentration of Vitamin C Serum?",
      "answer": "The concentration is 20%."
    },
    {
      "category": "Usage",
      "question": "What skin types is Vitamin C Serum suitable for?",
      "answer": "This product is suitable for dry, oily, combination skin types."
    },
    {
      "category": "Ingredients",
      "question": "What are the key ingredients in Vitamin C Serum?",
      "answer": "The key ingredients are: ascorbic acid, hyaluronic acid, vitamin E."
    },
    {
      "category": "Benefits",
      "question": "What are the benefits of using Vitamin C Serum?",
      "answer": "The benefits include: brightens skin, reduces wrinkles."
    },
    {
      "category": "Usage",
      "question": "How should I use Vitamin C Serum?",
      "answer": "Usage instructions: Apply daily in the morning."
    },
    {
      "category": "Safety",
      "question": "Are there any side effects associated with Vitamin C Serum?",
      "answer": "Side effects: mild irritation."
    },
    {
      "category": "Pricing",
      "question": "How much does Vitamin C Serum cost?",
      "answer": "The price is $29.99."
    }
  ]
}
```

#### Product Page (`outputs/product_page.json`)
```json
{
  "page_type": "product",
  "name": "Vitamin C Serum",
  "ingredients": ["ascorbic acid", "hyaluronic acid", "vitamin E"],
  "benefits": ["brightens skin", "reduces wrinkles"],
  "usage": "Apply daily in the morning",
  "side_effects": "mild irritation",
  "price": 29.99
}
```

#### Comparison Page (`outputs/comparison_page.json`)
```json
{
  "page_type": "comparison",
  "product_a": {
    "name": "Vitamin C Serum",
    "concentration": "20%",
    "skin_types": ["dry", "oily", "combination"],
    "ingredients": ["ascorbic acid", "hyaluronic acid", "vitamin E"],
    "benefits": ["brightens skin", "reduces wrinkles"],
    "usage_instructions": "Apply daily in the morning",
    "side_effects": "mild irritation",
    "price": 29.99
  },
  "product_b": {
    "name": "Hyaluronic Acid Moisturizer",
    "concentration": "2%",
    "skin_types": ["dry", "oily", "combination"],
    "ingredients": ["ascorbic acid", "hyaluronic acid", "glycerin", "aloe vera"],
    "benefits": ["hydrates skin", "reduces fine lines", "improves elasticity"],
    "usage_instructions": "Apply twice daily after cleansing",
    "side_effects": "Possible mild dryness",
    "price": 32.99
  }
}
```

## Example 2: Product with Null Values

### Input
```json
{
  "product_name": "MinimalCare Serum",
  "concentration": null,
  "skin_type": "Combination",
  "key_ingredients": "Hyaluronic Acid",
  "benefits": "Hydration",
  "how_to_use": "Apply once daily",
  "side_effects": null,
  "price": 399
}
```

### Key Differences
- No concentration question/answer.
- No safety question/answer.
- Skin type normalized to list.
- Price formatted as "$399.00".

## Example 3: Custom Input
You can create your own input JSON following the schema and run the system to generate outputs.