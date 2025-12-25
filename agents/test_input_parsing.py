#!/usr/bin/env python3
"""
Test script for InputParsingAgent
"""

import json
import sys
import os

# Add parent directory to path to import agents
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from agents.input_parsing_agent import InputParsingAgent

def test_input_parsing():
    # Load sample input
    with open('data/sample_input.json', 'r') as f:
        raw_input = json.load(f)

    # Create agent
    agent = InputParsingAgent()

    # Parse
    try:
        normalized = agent.parse(raw_input)
        print("Input parsing successful!")
        print("Normalized output:")
        print(json.dumps(normalized, indent=2))

        # Basic validation
        assert normalized['name'] == "Vitamin C Serum"
        assert normalized['concentration'] == "20%"
        assert normalized['skin_types'] == ["dry", "oily", "combination"]
        assert normalized['ingredients'] == ["ascorbic acid", "hyaluronic acid", "vitamin E"]
        assert normalized['benefits'] == ["brightens skin", "reduces wrinkles"]
        assert normalized['usage_instructions'] == "Apply daily in the morning"
        assert normalized['side_effects'] == "mild irritation"
        assert normalized['price'] == 29.99

        print("All validations passed!")

    except Exception as e:
        print(f"Error: {e}")
        return False

    return True

if __name__ == "__main__":
    test_input_parsing()