# Multi-Agent Product Content Generation System

This project implements a modular, agent-based automation system that converts structured product data into multiple machine-readable content pages (FAQ, Product Description, Comparison) using coordinated agents.

## Overview
- **Language**: Python 3.x
- **Architecture**: Modular classes for agents with single responsibilities
- **Agents**: Input Parsing, Question Generation, Content Logic, Assembly, Comparison, Orchestrator
- **Outputs**: faq.json, product_page.json, comparison_page.json
- **Deterministic**: Same input produces same output
- **No External Dependencies**: Uses only built-in Python libraries

## Features
- **Agent-Based Design**: Clear separation of concerns with no monolithic code
- **Robust Parsing**: Handles key variations and null values in input data
- **Content Generation**: Rule-based FAQ answers and structured pricing
- **Pure Assembly**: Template filling without logic or inference
- **Comprehensive Testing**: Individual agent tests and end-to-end validation

## Project Structure
```
kasparro-agentic-devikakp/
├── agents/                 # Agent classes
│   ├── __init__.py
│   ├── input_parsing_agent.py
│   ├── question_generation_agent.py
│   ├── content_logic_agents.py
│   ├── assembly_agents.py
│   ├── comparison_agent.py
│   ├── orchestrator_agent.py
│   └── test_*.py           # Individual agent tests
├── templates/              # JSON templates
│   ├── faq_template.json
│   ├── product_page_template.json
│   └── comparison_page_template.json
├── data/                   # Input data samples
│   ├── sample_input.json
│   ├── test_input1.json
│   ├── test_input2.json
│   └── test_input3.json
├── outputs/                # Generated JSON files
├── docs/                   # Documentation
│   └── projectdocumentation.md
├── main.py                 # Entry point
├── requirements.txt        # Dependencies (none)
└── README.md               # This file
```

## Installation
1. Ensure Python 3.x is installed.
2. Clone the repository:
   ```bash
   git clone https://github.com/devikakp-oss/kasparro-agentic-Devika-KP.git
   cd kasparro-agentic-devikakp
   ```
3. No additional dependencies required (uses built-in `json`).

## Usage
1. Prepare input data in JSON format (see `data/sample_input.json` for schema).
2. Run the system:
   ```bash
   python main.py
   ```
3. Outputs will be saved in `outputs/`:
   - `faq.json`: FAQ page with questions and answers
   - `product_page.json`: Product description page
   - `comparison_page.json`: Comparison with fictional competitor

### Input Schema
```json
{
  "name": "Product Name",
  "concentration": "10%",
  "skin_types": ["dry", "oily"],
  "ingredients": ["ingredient1", "ingredient2"],
  "benefits": ["benefit1", "benefit2"],
  "usage_instructions": "How to use",
  "side_effects": "Possible effects",
  "price": 29.99
}
```
- Fields are flexible; the system handles variations (e.g., `product_name`, null values).

### Running Tests
Run individual agent tests:
```bash
python agents/test_input_parsing.py
python agents/test_question_generation.py
python agents/test_content_logic.py
python agents/test_assembly.py
python agents/test_comparison.py
python agents/test_orchestrator.py
```

## Architecture
- **Input Parsing Agent**: Validates and normalizes raw input.
- **Question Generation Agent**: Creates customer questions from product data.
- **Content Logic Agents**: Generates reusable content blocks (usage, benefits, etc.).
- **Assembly Agents**: Purely maps data into JSON templates.
- **Comparison Agent**: Creates fictional competitor for comparison.
- **Orchestrator Agent**: Coordinates execution flow.

See `docs/projectdocumentation.md` for detailed specifications.

## Examples
### Sample Input
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

### Sample Output (FAQ)
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
    ...
  ]
}
```

## Contributing
1. Follow agent boundaries strictly.
2. Add tests for new functionality.
3. Ensure deterministic behavior.
4. Update documentation.

## License
This project is for educational purposes. See `docs/projectdocumentation.md` for full details.