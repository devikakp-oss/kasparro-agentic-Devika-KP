#!/usr/bin/env python3
"""
Test script for OrchestratorAgent
"""

import json
import sys
import os

# Add parent directory to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from agents.orchestrator_agent import OrchestratorAgent

def test_orchestrator():
    # Load sample input
    with open('data/sample_input.json', 'r') as f:
        raw_input = json.load(f)

    # Orchestrate
    orchestrator = OrchestratorAgent()
    outputs = orchestrator.orchestrate(raw_input)

    print("Orchestration successful!")
    print("Generated outputs:")
    print(f"FAQ: {len(outputs['faq']['faqs'])} questions")
    print(f"Product Page: {outputs['product_page']['name']}")
    print(f"Comparison Page: {outputs['comparison_page']['product_a']['name']} vs {outputs['comparison_page']['product_b']['name']}")

    # Basic validation
    assert 'faq' in outputs
    assert 'product_page' in outputs
    assert 'comparison_page' in outputs

    faq = outputs['faq']
    assert faq['page_type'] == 'faq'
    assert faq['product_name'] == 'Vitamin C Serum'
    assert len(faq['faqs']) >= 5

    product = outputs['product_page']
    assert product['page_type'] == 'product'
    assert product['name'] == 'Vitamin C Serum'
    assert isinstance(product['ingredients'], list)
    assert isinstance(product['benefits'], list)

    comparison = outputs['comparison_page']
    assert comparison['page_type'] == 'comparison'
    assert 'product_a' in comparison
    assert 'product_b' in comparison
    assert comparison['product_a']['name'] == 'Vitamin C Serum'
    assert comparison['product_b']['name'] == 'Hyaluronic Acid Moisturizer'

    print("All validations passed!")

    return True

if __name__ == "__main__":
    test_orchestrator()