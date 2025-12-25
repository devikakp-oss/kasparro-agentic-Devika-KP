#!/usr/bin/env python3
"""
Test script for AssemblyAgents
"""

import json
import sys
import os

# Add parent directory to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from agents.input_parsing_agent import InputParsingAgent
from agents.question_generation_agent import QuestionGenerationAgent
from agents.content_logic_agents import ContentLogicAgents
from agents.assembly_agents import AssemblyAgents

def test_assembly():
    # Load and process sample input through pipeline
    with open('data/sample_input.json', 'r') as f:
        raw_input = json.load(f)

    parsing_agent = InputParsingAgent()
    normalized = parsing_agent.parse(raw_input)

    question_agent = QuestionGenerationAgent()
    questions = question_agent.generate_questions(normalized)

    content_agent = ContentLogicAgents()
    blocks = content_agent.generate_blocks(normalized)

    # Assemble pages
    assembly_agent = AssemblyAgents()
    faq_page = assembly_agent.assemble_faq_page(questions, blocks, normalized)
    product_page = assembly_agent.assemble_product_page(blocks, normalized)

    print("Assembly successful!")
    print("\nFAQ Page:")
    print(json.dumps(faq_page, indent=2))
    print("\nProduct Page:")
    print(json.dumps(product_page, indent=2))

    # Basic validation
    assert faq_page['page_type'] == 'faq'
    assert faq_page['product_name'] == 'Vitamin C Serum'
    assert len(faq_page['faqs']) == len(questions)
    for faq in faq_page['faqs']:
        assert 'category' in faq
        assert 'question' in faq
        assert 'answer' in faq

    assert product_page['page_type'] == 'product'
    assert product_page['name'] == 'Vitamin C Serum'
    assert product_page['ingredients'] == blocks['ingredients']
    assert product_page['benefits'] == blocks['benefits']
    assert product_page['usage'] == blocks['usage']
    assert product_page['side_effects'] == blocks['safety']
    assert product_page['price'] == 29.99

    print("All validations passed!")

    return True

if __name__ == "__main__":
    test_assembly()