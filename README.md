# Self-Evaluating Lesson Generator using LangGraph

An AI-powered educational content generation system that creates, evaluates, and improves learning materials through an automated multi-agent workflow.

## Project Overview

The Self-Evaluating Lesson Generator is a Generative AI application designed to produce beginner-friendly educational lessons.

It uses LangGraph to coordinate three components:

- **Generator:** Creates educational lessons using Llama 3.2.
- **Evaluator:** Checks lesson quality against a predefined evaluation checklist.
- **Regenerator:** Improves rejected lessons using evaluator feedback.

The workflow automatically evaluates generated content and allows up to two regeneration retries when a lesson fails.

The application also uses SQLite to maintain persistent evaluation history and stores rejected lesson attempts in a rejection log.

## Technologies Used

- Python
- LangChain
- LangGraph
- Ollama
- Llama 3.2
- SQLite
- VS Code

## Key Features

### 1. Automated Lesson Generation
Generates beginner-friendly educational content based on a user-provided topic.

### 2. Lesson Evaluation
Evaluates lessons using a predefined checklist and assigns a score with pass/fail status.

### 3. Automatic Regeneration
Uses evaluator feedback to correct missing or incomplete content.

### 4. Conditional Workflow
LangGraph routes lessons based on their evaluation results.

### 5. Retry Management
Allows a maximum of two regeneration retries after the initial generation.

### 6. Persistent Memory
Uses SQLite to store previous lesson evaluations and feedback.

### 7. Rejection Logging
Records rejected lessons, evaluation scores, feedback, and attempt information.

### 8. Output Generation
Saves final generated lessons and evaluation results as text files.

## Project Architecture

```text
                 User Input
                     |
                     v
              Lesson Generator
                     |
                     v
               AI Evaluator
                     |
              Pass or Fail?
                /       \
              Pass      Fail
               |          |
               v          v
           Final       Regenerator
           Output          |
                           |
                           v
                       Evaluator
                           |
                    Maximum 2 Retries
```

## Project Structure

```text
self-evaluating-lesson-generator/
│
├── agents/
│   ├── generator.py
│   ├── evaluator.py
│   └── regenerator.py
│
├── memory/
│   ├── database.py
│   └── lesson_memory.db
│
├── outputs/
│   ├── generated_lessons.txt
│   └── rejection_log.txt
│
├── workflow/
│   ├── __init__.py
│   └── graph.py
│
├── config.py
├── requirements.txt
├── README.md
└── .gitignore
```

*Note: Generated output files and the SQLite database are created during execution.*

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/sidhartha315/self-evaluating-lesson-generator.git
```

### 2. Navigate to the project

```bash
cd self-evaluating-lesson-generator
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

### 4. Activate the environment

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

### 5. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 6. Install Ollama

Install Ollama and download the Llama 3.2 model:

```bash
ollama pull llama3.2
```

Make sure Ollama is running before executing the application.

### 7. Run the application

From the project root directory:

```bash
python -m workflow.graph
```

## Example Input

```text
Introduction to RAG
```

## Example Output

The application generates:

- A complete educational lesson.
- Evaluation score.
- Pass/fail status.
- Evaluator feedback.
- Number of regeneration retries.
- Saved lesson output.

Example evaluation:

```text
Topic: Introduction to RAG
Score: 100
Passed: True
Attempts: 0
Feedback: []
```

## Persistent Memory and Learning

The application uses SQLite to maintain lesson evaluation history.

Previous evaluation failures can be retrieved and supplied to the generator as feedback for future lesson generation.

Rejected lessons are also recorded in:

```text
outputs/rejection_log.txt
```

This supports feedback-based improvement across multiple executions.

## Project Objective

The objective is to demonstrate how Generative AI agents can collaborate to create educational content, evaluate its quality, improve failed outputs, and maintain historical feedback.

## Author

**Rachamalla Sidhartha**

Aspiring AI Engineer | Generative AI Developer

GitHub: https://github.com/sidhartha315