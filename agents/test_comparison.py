#!/usr/bin/env python3
"""
Test script for ComparisonAgent
"""

import json
import sys
import os

# Add parent directory to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from agents.input_parsing_agent import InputParsingAgent
from agents.comparison_agent import ComparisonAgent

def test_comparison():
    # Load and parse sample input
    with open('data/sample_input.json', 'r') as f:
        raw_input = json.load(f)

    parsing_agent = InputParsingAgent()
    product_a = parsing_agent.parse(raw_input)

    # Generate Product B
    comparison_agent = ComparisonAgent()
    product_b = comparison_agent.generate_product_b(product_a)

    print("Comparison agent successful!")
    print("Product A:")
    print(json.dumps(product_a, indent=2))
    print("\nProduct B:")
    print(json.dumps(product_b, indent=2))

    # Basic validation
    required_keys = ['name', 'concentration', 'skin_types', 'ingredients', 'benefits', 'usage_instructions', 'side_effects', 'price']
    for key in required_keys:
        assert key in product_b, f"Missing key: {key}"

    # Schema parity
    assert isinstance(product_b['name'], str)
    assert isinstance(product_b['concentration'], str)
    assert isinstance(product_b['skin_types'], list)
    assert isinstance(product_b['ingredients'], list)
    assert isinstance(product_b['benefits'], list)
    assert isinstance(product_b['usage_instructions'], str)
    assert isinstance(product_b['side_effects'], str)
    assert isinstance(product_b['price'], (int, float))

    # Specific rules
    assert product_b['name'] != product_a['name'], "Product B name should be different"
    assert product_b['skin_types'] == product_a['skin_types'], "Skin types should match"
    shared = set(product_a['ingredients']) & set(product_b['ingredients'])
    assert len(shared) > 0, "Should have partial ingredient overlap"
    assert product_b['price'] != product_a['price'], "Price should differ"
    assert 0.8 * product_a['price'] <= product_b['price'] <= 1.2 * product_a['price'], "Price difference within 20%"

    print("All validations passed!")

    return True

if __name__ == "__main__":
    test_comparison()