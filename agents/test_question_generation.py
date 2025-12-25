#!/usr/bin/env python3
"""
Test script for QuestionGenerationAgent
"""

import json
import sys
import os

# Add parent directory to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from agents.input_parsing_agent import InputParsingAgent
from agents.question_generation_agent import QuestionGenerationAgent

def test_question_generation():
    # Load sample input
    with open('data/sample_input.json', 'r') as f:
        raw_input = json.load(f)

    # Parse input
    parsing_agent = InputParsingAgent()
    normalized = parsing_agent.parse(raw_input)

    # Generate questions
    question_agent = QuestionGenerationAgent()
    questions = question_agent.generate_questions(normalized)

    print("Question generation successful!")
    print(f"Generated {len(questions)} questions:")
    for i, q in enumerate(questions, 1):
        print(f"{i}. [{q['category']}] {q['question']}")

    # Basic validation
    assert len(questions) >= 5, "Should generate at least 5 questions"
    categories = {q['category'] for q in questions}
    expected_categories = {"General", "Ingredients", "Usage", "Benefits", "Safety", "Pricing"}
    assert categories.issubset(expected_categories), f"Unexpected categories: {categories - expected_categories}"

    # Check specific questions
    question_texts = [q['question'] for q in questions]
    assert any("name" in q.lower() for q in question_texts), "Should have name question"
    assert any("concentration" in q.lower() for q in question_texts), "Should have concentration question"
    assert any("skin types" in q.lower() for q in question_texts), "Should have skin types question"
    assert any("ingredients" in q.lower() for q in question_texts), "Should have ingredients question"
    assert any("benefits" in q.lower() for q in question_texts), "Should have benefits question"
    assert any("use" in q.lower() for q in question_texts), "Should have usage question"
    assert any("side effects" in q.lower() for q in question_texts), "Should have side effects question"
    assert any("cost" in q.lower() for q in question_texts), "Should have price question"

    print("All validations passed!")

    return True

if __name__ == "__main__":
    test_question_generation()