# System Architecture

This document describes the architecture of the Multi-Agent Product Content Generation System.

## Agent Overview
The system uses a multi-agent architecture with clear boundaries and single responsibilities.

### 1. Input Parsing Agent (`input_parsing_agent.py`)
- **Responsibility**: Validate and normalize raw product input.
- **Input**: Raw JSON dict
- **Output**: Normalized internal product model (dict)
- **Key Features**:
  - Handles key variations (e.g., `product_name` → `name`)
  - Normalizes lists from comma-separated strings
  - Converts prices to float
  - Validates required fields

### 2. Question Generation Agent (`question_generation_agent.py`)
- **Responsibility**: Generate customer-style questions from product data.
- **Input**: Normalized product model
- **Output**: List of question dicts (category, question)
- **Key Features**:
  - Rule-based generation
  - Categorized questions (General, Ingredients, Usage, etc.)
  - Deterministic output

### 3. Content Logic Agents (`content_logic_agents.py`)
- **Responsibility**: Create reusable content blocks.
- **Input**: Normalized product model
- **Output**: Dict of content blocks
- **Blocks**:
  - `usage`: Usage instructions (string)
  - `benefits`: List of benefits
  - `ingredients`: List of ingredients
  - `safety`: Side effects (string)
  - `pricing`: Structured pricing (dict with display and value)

### 4. Assembly Agents (`assembly_agents.py`)
- **Responsibility**: Purely map data into JSON templates.
- **Inputs**: Questions, answers, blocks, product data
- **Outputs**: JSON pages
- **Key Features**:
  - No logic or parsing
  - Mechanical template filling
  - Three methods: FAQ, Product, Comparison assembly

### 5. Comparison Agent (`comparison_agent.py`)
- **Responsibility**: Generate fictional competitor product.
- **Input**: Product A model
- **Output**: Product B model
- **Key Features**:
  - Mirrors schema
  - Partial ingredient overlap
  - Controlled price difference

### 6. Orchestrator Agent (`orchestrator_agent.py`)
- **Responsibility**: Coordinate execution flow.
- **Input**: Raw input
- **Output**: Dict of all JSON outputs
- **Key Features**:
  - Calls agents in sequence
  - No content logic
  - Ensures pipeline completion

## Data Flow
```
Raw Input
    ↓
Input Parsing → Normalized Product
    ↓
Question Generation → Questions
Content Logic → Content Blocks
    ↓
Assembly (FAQ) → FAQ JSON
Assembly (Product) → Product JSON
Comparison → Product B
Assembly (Comparison) → Comparison JSON
```

## Design Principles
- **Single Responsibility**: Each agent has one clear task.
- **Deterministic**: Same input → same output.
- **Modular**: Agents are independent and testable.
- **No Global State**: Data passed explicitly.
- **Pure Assembly**: Assembly agents only map, no logic.

## Testing Strategy
- Unit tests for each agent.
- Integration tests for orchestrator.
- Validation of input/output contracts.
- Edge case testing (nulls, variations).

## Extensibility
- Add new agents by following boundaries.
- Extend parsing for new fields.
- Modify content logic for different rules.
- Keep assembly pure for new templates.