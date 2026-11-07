# Self-Evaluating Lesson Generator using LangGraph

## Project Overview

The Self-Evaluating Lesson Generator is an AI-powered application that automatically creates educational lessons, evaluates their quality, and improves them based on AI-generated feedback.

It uses LangGraph to manage multiple AI agents in a workflow and Ollama to run the Llama 3.2 language model locally.

## Technologies Used

- Python
- LangChain
- LangGraph
- Ollama
- Llama 3.2
- SQLite / Database (if configured)
- VS Code

## Key Features

1. **Lesson Generation:** Generates beginner-friendly educational lessons based on a given topic.
2. **AI Evaluation:** Evaluates generated lessons and assigns a quality score.
3. **Automatic Regeneration:** Improves lessons using evaluator feedback.
4. **Conditional Routing:** Uses LangGraph to decide whether a lesson passes or needs improvement.
5. **Self-Evaluation:** Repeats the evaluation process until the lesson passes or reaches the maximum number of attempts.
6. **Output Generation:** Saves generated lessons as text files.

## Project Architecture

The application follows a multi-agent workflow:

User Input → Lesson Generator → AI Evaluator → Conditional Router

If the lesson fails:

Evaluator → Lesson Regenerator → Evaluator

If the lesson passes:

Evaluator → Final Output

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
│   └── database.py
│
├── outputs/
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

## Installation

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Navigate to the project

```bash
cd self-evaluating-lesson-generator
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the environment

Windows:

```bash
venv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Install and run Ollama

Pull the model:

```bash
ollama pull llama3.2
```

### 7. Run the project

```bash
python workflow/graph.py
```

## Example Input

```text
Introduction to RAG
```

## Example Output

- Generated educational lesson
- Evaluation score
- Pass/fail status
- Improvement feedback
- Number of regeneration attempts

## Project Outcome

Successfully implemented an AI-powered self-evaluating lesson generation workflow using LangGraph and Ollama.

The project demonstrates multi-agent collaboration, conditional execution, automated evaluation, and iterative content improvement.

## Author

Rachamalla Sidhartha

Aspiring AI Engineer | Generative AI Developer