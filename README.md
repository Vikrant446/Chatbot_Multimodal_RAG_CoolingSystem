
#### Problem Statement & Requirements : To design, build, and deploy an end-to-end Multimodal Retrieval-Augmented Generation (RAG) system that solves a real problem related to vehicle cooling systems and thermal management.
--------------------------------------------------------------------------------------------------
## Domain Identification

The domain of this project is Automotive Engineering, with a specific focus on vehicle cooling systems and thermal management.

Modern automotive systems involve complex multimodal technical documentation, including:

* Engineering manuals
* System diagrams (radiators, coolant flow paths)
* Performance charts
* Maintenance guidelines

Professionals such as: Automotive engineers, Service technicians, Mechanical students often rely on these documents for diagnostics, design understanding, and troubleshooting.
--------------------------------------------------------------------------------------------------

## Problem Description

In automotive engineering, extracting precise information from cooling system documentation is challenging and time-consuming.

**Key Issues:

1.Multimodal Content Complexity

   * The cooling system PDF contains:
    > Text descriptions (working principles)
    > Diagrams (coolant flow, radiator structure)
    > Tables (temperature ranges, specifications)
   * Traditional search tools cannot interpret diagrams or relate them to text.

2.Unstructured Information

   * Information is scattered across: Sections, Figures, Technical notes
     
   * Users must manually read and correlate content.

3. Inefficient Querying

   * Queries like:
     > “What happens if coolant flow is blocked?”
     > “Explain radiator working with diagram reference”
   Cannot be answered directly using keyword search.

4.Time-Consuming Troubleshooting

   * Technicians must scan entire manuals to diagnose faults.
--------------------------------------------------------------------------------------------------

## Why This Problem Is Unique

This problem goes beyond a generic document Q&A system due to domain-specific challenges:

 1. Engineering Terminology

Terms like:Thermostat valve, Coolant circulation, Heat dissipation
 Require contextual understanding, not just keyword matching.

2. Diagram + Text Dependency

Cooling system understanding depends heavily on: Flow diagrams, Component layouts.
Traditional systems cannot link diagrams with explanations.

3. Technical Tables & Specifications

Data like:Temperature limits, Pressure values often appear in structured tables that require interpretation.

4. Cause-Effect Relationships
Example:
“Overheating → coolant failure → engine damage”
Requires reasoning across multiple sections.
--------------------------------------------------------------------------------------------------

## Why RAG Is the Right Approach

Retrieval-Augmented Generation (RAG)system is ideal for this problem due to the following reasons:

1. Context-Aware Retrieval
* Retrieves relevant sections from the PDF
* Ensures answers are grounded in actual technical content

2. Combines Retrieval + Reasoning

Unlike keyword search:
RAG understands semantic meaning
Generates human-readable explanations

3. Handles Multimodal Data (with Extensions)
Can integrate: Text embeddings, Image embeddings (future scope), Enables diagram-aware responses.

4. Avoids Costly Fine-Tuning
No need to retrain large models
Works dynamically with updated documents

5. Reduces Hallucination: Responses are based on retrieved context → higher accuracy
--------------------------------------------------------------------------------------------------

## Expected Outcomes

A successful RAG-based cooling system chatbot should:

1. Answer Technical Queries

Examples:

* “Explain the working of a radiator”
* “What causes engine overheating?”
* “What is the role of coolant in heat transfer?”

2. Assist in Troubleshooting

* Identify possible causes of: Overheating, Coolant leakage.
* Suggest explanations based on document knowledge

3. Provide Contextual Explanations

* Combine: Text + related sections
* Deliver step-by-step explanations

4. Improve Efficiency

* Reduce manual document reading time
* Enable quick information retrieval

5. Support Decision-Making

* Helps:

  * Engineers → system design understanding
  * Technicians → fault diagnosis
  * Students → conceptual clarity
--------------------------------------------------------------------------------------------------

## Summary

This project aims to build a domain-specific multimodal RAG chatbot for automotive cooling systems that:

* Bridges the gap between complex engineering documents and user queries
* Enables intelligent, context-aware information retrieval
* Improves efficiency, accuracy, and usability in technical workflows

--------------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------------

#### Simple RAG Architecture Block Diagram
 
            ┌──────────────────────────┐
            │   Cooling System PDF     │
            │ (Text + Images + Tables)│
            └───────────┬──────────────┘
                        │
                        ▼
            ┌──────────────────────────┐
            │   Data Ingestion Layer   │
            │ (PDF Loader, OCR, Parser)│
            └───────────┬──────────────┘
                        │
                        ▼
            ┌──────────────────────────┐
            │     Text Chunking        │
            │ (Split into small parts) │
            └───────────┬──────────────┘
                        │
                        ▼
            ┌──────────────────────────┐
            │     Embedding Model      │
            │ (Convert text → vectors) │
            └───────────┬──────────────┘
                        │
                        ▼
            ┌──────────────────────────┐
            │      Vector Database     │
            │   (FAISS / Chroma DB)   │
            └───────────┬──────────────┘
                        │
        ┌───────────────┴───────────────┐
        │                               │
        ▼                               ▼
┌───────────────────┐         ┌────────────────────┐
│     User Query    │         │   Stored Embeddings│
└─────────┬─────────┘         └─────────┬──────────┘
          │                               │
          ▼                               │
┌──────────────────────────┐              │
│   Query Embedding Model  │◄─────────────┘
└───────────┬──────────────┘
            │
            ▼
┌──────────────────────────┐
│   Similarity Search      │
│ (Top-K Relevant Chunks)  │
└───────────┬──────────────┘
            │
            ▼
┌──────────────────────────┐
│    LLM (GPT / LLaMA)     │
│ (Generate Final Answer)  │
└───────────┬──────────────┘
            │
            ▼
┌──────────────────────────┐
│     Final Response       │
│ (Accurate + Contextual)  │
└──────────────────────────┘
--------------------------------------------------------------------------------------------------

## Technology Choices

This section justifies the selection of each major component used in the RAG system.

1. PDF Parser — PyMuPDF (fitz)
*Why chosen:
Efficient extraction of text + images from engineering PDFs
Preserves page-level structure, useful for traceability
Faster than alternatives like PDFMiner
* Relevance to Cooling System PDF:
The document contains:
Technical explanations (text)
Cooling system diagrams (images)
PyMuPDF enables extraction of both modalities

2 Embedding Model — Sentence Transformers (all-MiniLM-L6-v2)
* Why chosen:
Lightweight and fast (important for Codespaces)
Good semantic understanding of technical queries
Works offline (no API dependency)
* Use in this project:
Converts:
Cooling system concepts (e.g., radiator, coolant flow)
User queries into vector representations for similarity search

3 Vector Database — ChromaDB
* Why chosen:
Easy integration with Python
No external server required
Supports metadata (page number, type)
* Use in this project:
Stores:
Text chunks from PDF
Image descriptions
Enables fast retrieval of relevant cooling system knowledge

4 LLM (Language Model) — Lightweight Local LLM / Rule-based Generator
* Why chosen:
No API cost
Simple implementation for assignment scope
Can be upgraded later to advanced models (GPT-4, LLaMA)
* Role:
Generates final answers using:
Retrieved chunks
Context from cooling system document

5 VLM (Vision-Language Model) — Simulated Vision Module
* Why chosen:
Assignment-level implementation constraint
Avoids heavy GPU requirements
* Role:
Converts diagrams into textual descriptions like:
“Radiator connected to coolant flow system”

* Future upgrade:
Replace with real VLM (e.g., GPT-4o Vision)
--------------------------------------------------------------------------------------------------

## Setup Instructions (GitHub Codespaces)
Step 1: Clone Repository
git clone https://github.com/your-username/multimodal-rag-cooling-system.git
cd multimodal-rag-cooling-system

Step 2: Install Dependencies
pip install -r requirements.txt

Step 3: Project Structure
project/
│── src/
│   ├── ingestion/
│   ├── retrieval/
│   ├── models/
│── sample_documents/
│   └── Cooling_System.pdf
│── main.py
│── requirements.txt

Step 4: Run Application
uvicorn main:app --host 0.0.0.0 --port 8000

Step 5: Open in Browser
http://localhost:8000/docs

Step 6: Run Pipeline
Upload PDF → /ingest
Ask query → /query
--------------------------------------------------------------------------------------------------

## API Documentation
1. Health Check
Endpoint:
GET /health
Response:
{
  "status": "ok",
  "uptime": 120.5
}

2. Document Ingestion
Endpoint: POST /ingest
Request: Form-data → Upload PDF file
Response:
{
  "message": "done"
}

3. Query Endpoint
Endpoint: POST /query?q=What is radiator?
Response:
{
  "answer": "The radiator is responsible for heat dissipation..."
}
--------------------------------------------------------------------------------------------------

## Screenshots (What to Include)

(UNABLE TO RUN THE CODESPACE DUE TO HARDWARE ISSUE)

*Required Screenshots:
Swagger UI (/docs)
PDF Upload Success (/ingest)
Query Response Example
Health API Output

* Example Queries to Show:
“Explain cooling system working”
“What causes overheating?”
“Role of coolant in engine?”
--------------------------------------------------------------------------------------------------

## Limitations & Future Work
1. Limitations
A. Basic Image Understanding
Current system uses dummy image captions
Cannot truly interpret diagrams
B. Limited LLM Capability
Response generation is simplified
Lacks deep reasoning
C. No OCR for Complex Tables
Tables with structured data may not be fully understood
D. Small Embedding Model
May miss nuanced technical relationships
E. No Real-Time Learning
System does not update dynamically after deployment
--------------------------------------------------------------------------------------------------

##Future Improvements
A. Integrate Advanced LLM
Use GPT-4 / LLaMA for better reasoning
B. Add Real Vision Model
Use GPT-4o Vision for diagram understanding
C. Improve Retrieval
Hybrid search (keyword + vector)
D. Add OCR & Table Parsing
Extract structured data from:Charts, Tables
E. UI Development
Build frontend chatbot interface
F. Evaluation Metrics
Integrate:RAGAS, Faithfulness, Answer relevance
--------------------------------------------------------------------------------------------------
