#!/usr/bin/env python3
"""
Main entry point for the Multi-Agent Content Generation System.
Loads input, orchestrates the pipeline, and saves outputs.
"""

import json
import os
from agents.orchestrator_agent import OrchestratorAgent

def main():
    # Load raw input
    input_path = 'data/sample_input.json'
    if not os.path.exists(input_path):
        print(f"Error: Input file {input_path} not found.")
        return

    with open(input_path, 'r') as f:
        raw_input = json.load(f)

    # Orchestrate
    orchestrator = OrchestratorAgent()
    outputs = orchestrator.orchestrate(raw_input)

    # Save outputs
    os.makedirs('outputs', exist_ok=True)

    with open('outputs/faq.json', 'w') as f:
        json.dump(outputs['faq'], f, indent=2)

    with open('outputs/product_page.json', 'w') as f:
        json.dump(outputs['product_page'], f, indent=2)

    with open('outputs/comparison_page.json', 'w') as f:
        json.dump(outputs['comparison_page'], f, indent=2)

    print("Pipeline completed successfully!")
    print("Outputs saved to outputs/ directory:")
    print("- faq.json")
    print("- product_page.json")
    print("- comparison_page.json")

if __name__ == "__main__":
    main()