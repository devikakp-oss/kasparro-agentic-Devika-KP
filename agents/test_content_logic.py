#!/usr/bin/env python3
"""
Test script for ContentLogicAgents
"""

import json
import sys
import os

# Add parent directory to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from agents.input_parsing_agent import InputParsingAgent
from agents.content_logic_agents import ContentLogicAgents

def test_content_logic():
    # Load and parse sample input
    with open('data/sample_input.json', 'r') as f:
        raw_input = json.load(f)

    parsing_agent = InputParsingAgent()
    normalized = parsing_agent.parse(raw_input)

    # Generate content blocks
    content_agent = ContentLogicAgents()
    blocks = content_agent.generate_blocks(normalized)

    print("Content logic generation successful!")
    print("Generated blocks:")
    print(json.dumps(blocks, indent=2))

    # Basic validation
    assert 'usage' in blocks
    assert 'benefits' in blocks
    assert 'ingredients' in blocks
    assert 'safety' in blocks
    assert 'pricing' in blocks

    # Check types
    assert isinstance(blocks['usage'], str)
    assert isinstance(blocks['benefits'], list)
    assert isinstance(blocks['ingredients'], list)
    assert isinstance(blocks['safety'], str)
    assert isinstance(blocks['pricing'], str)

    # Check content
    assert blocks['usage'] == "Apply daily in the morning"
    assert blocks['benefits'] == ["brightens skin", "reduces wrinkles"]
    assert blocks['ingredients'] == ["ascorbic acid", "hyaluronic acid", "vitamin E"]
    assert blocks['safety'] == "mild irritation"
    assert blocks['pricing'] == "$29.99"

    print("All validations passed!")

    return True

if __name__ == "__main__":
    test_content_logic()