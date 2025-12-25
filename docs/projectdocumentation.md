# Multi-Agent Product Content Generation System

## 1. Problem Statement
The objective of this project is to design and implement a modular, agent-based automation system that converts structured product data into multiple machine-readable content pages. The system must operate exclusively on the provided input data and generate outputs via coordinated agents rather than a monolithic script.

The system produces three outputs:
- FAQ Page (JSON)
- Product Description Page (JSON)
- Product Comparison Page (JSON)

The focus of this assignment is system design, agent orchestration, reusable logic, and structured output generation.

---

## 2. Solution Overview
This solution implements a deterministic, multi-agent pipeline. Raw product input is normalized into an internal data model, customer-relevant questions are generated, reusable content logic blocks are created, structured templates are defined, and final JSON pages are assembled. An orchestrator agent controls execution order and data flow.

All transformations are rule-based, traceable, and derived solely from the provided input data.

---

## 3. Input Data Schema

### 3.1 Raw Input
The system accepts structured product data containing only the fields provided in the assignment. No additional fields are introduced.

### 3.2 Internal Product Model
All agents operate on a normalized internal representation with the following schema:

- `name` (string)
- `concentration` (string | null)
- `skin_types` (list[string])
- `ingredients` (list[string])
- `benefits` (list[string])
- `usage_instructions` (string)
- `side_effects` (string | null)
- `price` (number)

**Validation**
- Required fields must exist
- Lists are normalized from comma-separated strings
- Numeric values are converted to numbers
- No new facts are inferred or added

---

## 4. Technology & Implementation Assumptions

- Language: Python
- Architecture: Modular Python modules/classes
- Agent Communication: In-memory Python objects
- No external agent frameworks (e.g., LangChain, CrewAI)
- No databases, files, or shared global state

These choices prioritize transparency, determinism, and explicit agent boundaries.

---

## 5. Agent Architecture

### 5.1 Input Parsing Agent
**Responsibility**
- Validate and normalize raw product input
- Produce internal product model

**Validation**
- Field presence and type checks
- Graceful handling of optional fields

---

### 5.2 Question Generation Agent
**Responsibility**
- Generate customer-style questions using rule-based logic
- Categorize questions (Usage, Safety, Ingredients, Pricing, etc.)

**Validation**
- Questions are derived directly from product attributes
- No hardcoded or manually authored questions
- Minimum question count enforced

---

### 5.3 Content Logic Agents
Reusable logic blocks include:
- Usage Block
- Benefits Block
- Ingredients Block
- Safety Block
- Pricing Block

**Responsibility**
- Transform product data into reusable content units

**Validation**
- Single-responsibility enforcement
- Blocks reused across multiple page types
- No page-specific formatting

---

## 6. Template Definitions

Templates define structure only and contain no content logic.

### 6.1 FAQ Page Template
```json
{
  "page_type": "faq",
  "product_name": "string",
  "faqs": [
    {
      "category": "string",
      "question": "string",
      "answer": "string"
    }
  ]
}
```

⸻

6.2 Product Page Template

{
  "page_type": "product",
  "name": "string",
  "ingredients": ["string"],
  "benefits": ["string"],
  "usage": "string",
  "side_effects": "string",
  "price": "number"
}


⸻

6.3 Comparison Page Template

{
  "page_type": "comparison",
  "product_a": { "..." },
  "product_b": { "..." }
}


⸻

7. Assembly Agents

Assembly agents populate templates using prepared content blocks.

Assembly Rules
	•	No content generation
	•	No logic or inference
	•	Pure structural mapping

Outputs
	•	faq.json
	•	product_page.json
	•	comparison_page.json

⸻

8. Fictional Product Comparison

Comparison Agent

Responsibility
	•	Generate a fictional Product B for comparison

Product B Generation Rules
	•	Mirrors Product A schema
	•	Belongs to same product category
	•	Shares partial ingredient overlap
	•	Price differs within a controlled range
	•	No qualitative or superiority claims

Validation
	•	Schema parity with Product A
	•	No real products or external data used

⸻

9. Orchestrator Agent

Responsibility
	•	Control execution order
	•	Pass outputs between agents
	•	Ensure full pipeline completion

Agents do not communicate directly. All data flow is mediated by the orchestrator.

⸻

10. Orchestration Flow

Raw Input
   ↓
Input Parsing Agent
   ↓
Internal Product Model
   ↓
Question Generation Agent
   ↓
Content Logic Blocks
   ↓
Template Definitions
   ↓
Assembly Agents
   ↓
Comparison Agent
   ↓
Final JSON Outputs


⸻

11. Validation & Correctness Strategy

This system is evaluated based on engineering correctness rather than statistical ML metrics.

Correctness is ensured through:
	•	Explicit input/output contracts per agent
	•	Schema validation at each stage
	•	Deterministic execution (same input → same output)
	•	Traceability of all output fields back to input data
	•	Reusability testing with schema-compatible inputs during development

No accuracy, precision, recall, or probabilistic metrics are applied, as the system performs deterministic transformations rather than predictive inference.

⸻

12. Design Principles
	•	Single Responsibility Principle
	•	Clear agent boundaries
	•	Deterministic behavior
	•	No hidden global state
	•	Modular and extensible architecture

⸻

13. Summary

This project demonstrates a production-style agentic system that converts structured product data into multiple machine-readable content pages using reusable logic, template-driven generation, and explicit orchestration. The system prioritizes correctness, clarity, and extensibility over content creativity or model-based performance metrics.

---