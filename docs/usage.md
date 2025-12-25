# Usage Guide

This guide provides detailed instructions for using the Multi-Agent Product Content Generation System.

## Quick Start
1. Clone the repository and navigate to the folder.
2. Ensure Python 3.x is installed.
3. Run `python main.py` with sample data.
4. Check `outputs/` for generated JSON files.

## Input Data Preparation
The system accepts product data in JSON format. The schema is flexible, but recommended fields are:

- `name` (string): Product name
- `concentration` (string, optional): Product concentration
- `skin_types` (array or comma-separated string): Suitable skin types
- `ingredients` (array or comma-separated string): Key ingredients
- `benefits` (array or comma-separated string): Product benefits
- `usage_instructions` (string): How to use the product
- `side_effects` (string, optional): Possible side effects
- `price` (number): Product price

### Example Input
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

### Supported Variations
- Key names: `product_name` instead of `name`, `key_ingredients` instead of `ingredients`, `how_to_use` instead of `usage_instructions`
- Null values: Optional fields can be `null` or omitted
- Data types: Strings are normalized; prices are converted to float

## Running the System
1. Place your input JSON in `data/` (e.g., `my_input.json`).
2. Edit `main.py` to load your file:
   ```python
   input_path = 'data/my_input.json'
   ```
3. Run:
   ```bash
   python main.py
   ```

## Output Files
- `outputs/faq.json`: FAQ page with categorized questions and answers
- `outputs/product_page.json`: Product details page
- `outputs/comparison_page.json`: Comparison with a fictional competitor

### Output Schemas
See `templates/` for the exact JSON structures.

## Testing
Run all tests to ensure functionality:
```bash
python agents/test_input_parsing.py
python agents/test_question_generation.py
python agents/test_content_logic.py
python agents/test_assembly.py
python agents/test_comparison.py
python agents/test_orchestrator.py
```

## Troubleshooting
- **Error: Required field missing**: Ensure all required fields are present in input.
- **No output generated**: Check input JSON syntax.
- **Test failures**: Verify Python version and file paths.

## Customization
- Modify agents in `agents/` for custom logic (maintain single responsibility).
- Add new templates in `templates/`.
- Extend input parsing for new fields.

For architecture details, see `docs/projectdocumentation.md`.