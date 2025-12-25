# Agent Flow Visualization

This document contains visualizations of the Multi-Agent Product Content Generation System flow.

## Overall System Flow

```mermaid
graph TD
    A[Raw Product Input] --> B[Input Parsing Agent]
    B --> C[Normalized Product Model]
    C --> D[Question Generation Agent]
    C --> E[Content Logic Agents]
    D --> F[Questions]
    E --> G[Content Blocks]
    F --> H[Assembly Agents - FAQ]
    G --> H
    C --> H
    H --> I[FAQ JSON]
    G --> J[Assembly Agents - Product]
    C --> J
    J --> K[Product JSON]
    C --> L[Comparison Agent]
    L --> M[Product B Model]
    C --> N[Assembly Agents - Comparison]
    M --> N
    N --> O[Comparison JSON]
    I --> P[Orchestrator Output]
    K --> P
    O --> P
```

## Agent Interaction Flow

```mermaid
graph TD
    subgraph "Orchestrator Agent"
        O1[Receive Raw Input]
        O2[Call Input Parsing]
        O3[Call Question Generation]
        O4[Call Content Logic]
        O5[Call Assembly FAQ]
        O6[Call Assembly Product]
        O7[Call Comparison]
        O8[Call Assembly Comparison]
        O9[Return Outputs]
    end

    O1 --> O2
    O2 --> O3
    O3 --> O4
    O4 --> O5
    O5 --> O6
    O6 --> O7
    O7 --> O8
    O8 --> O9

    subgraph "Input Parsing Agent"
        P1[Validate Input]
        P2[Normalize Data]
        P3[Return Model]
    end

    O2 --> P1
    P1 --> P2
    P2 --> P3
    P3 --> O3

    subgraph "Question Generation Agent"
        Q1[Analyze Product Data]
        Q2[Generate Questions]
        Q3[Return Questions]
    end

    O3 --> Q1
    Q1 --> Q2
    Q2 --> Q3
    Q3 --> O4

    subgraph "Content Logic Agents"
        C1[Generate Usage Block]
        C2[Generate Benefits Block]
        C3[Generate Ingredients Block]
        C4[Generate Safety Block]
        C5[Generate Pricing Block]
        C6[Return Blocks]
    end

    O4 --> C1
    C1 --> C2
    C2 --> C3
    C3 --> C4
    C4 --> C5
    C5 --> C6
    C6 --> O5

    subgraph "Assembly Agents"
        A1[Assemble FAQ]
        A2[Assemble Product]
        A3[Assemble Comparison]
    end

    O5 --> A1
    O6 --> A2
    O8 --> A3

    subgraph "Comparison Agent"
        Comp1[Mirror Product A]
        Comp2[Generate Product B]
        Comp3[Return Product B]
    end

    O7 --> Comp1
    Comp1 --> Comp2
    Comp2 --> Comp3
    Comp3 --> O8
```

## Data Transformation Flow

```mermaid
graph LR
    A[Raw JSON Input] --> B[Input Parsing]
    B --> C[Normalized Dict]
    C --> D[Question Generation]
    D --> E[Questions List]
    C --> F[Content Logic]
    F --> G[Blocks Dict]
    E --> H[Assembly FAQ]
    G --> H
    C --> H
    H --> I[FAQ JSON]
    G --> J[Assembly Product]
    C --> J
    J --> K[Product JSON]
    C --> L[Comparison]
    L --> M[Product B Dict]
    C --> N[Assembly Comparison]
    M --> N
    N --> O[Comparison JSON]
```

## Agent Responsibility Matrix

```mermaid
graph TD
    A[Input Parsing Agent] --> B[Validation & Normalization]
    C[Question Generation Agent] --> D[Question Creation]
    E[Content Logic Agents] --> F[Reusable Blocks]
    G[Assembly Agents] --> H[Pure Mapping]
    I[Comparison Agent] --> J[Fictional Product]
    K[Orchestrator Agent] --> L[Flow Control]
```

These diagrams show the modular, agent-based architecture with clear data flow and responsibilities.