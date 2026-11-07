import os
import re
from datetime import datetime
from typing import TypedDict

from langgraph.graph import StateGraph, START, END

from agents.generator import generate_lesson
from agents.evaluator import evaluate_lesson
from agents.regenerator import regenerate_lesson

from memory.database import (
    save_run,
    get_learning_notes,
    save_rejection
)


# ==========================================
# WORKFLOW STATE
# ==========================================

class LessonState(TypedDict):
    topic: str
    lesson: str
    score: int
    feedback: list
    attempts: int
    passed: bool


# ==========================================
# GENERATOR
# ==========================================

def generate_node(state: LessonState):

    learning_notes = get_learning_notes(state["topic"])

    lesson = generate_lesson(
        state["topic"],
        learning_notes
    )

    return {
        "lesson": lesson,
        "attempts": 0
    }


# ==========================================
# EVALUATOR
# ==========================================

def evaluate_node(state: LessonState):

    evaluation = evaluate_lesson(state["lesson"])

    if not evaluation["passed"]:

        save_rejection(
            state["topic"],
            state["lesson"],
            evaluation["score"],
            evaluation["feedback"],
            state["attempts"] + 1
        )

    return {
        "score": evaluation["score"],
        "feedback": evaluation["feedback"],
        "passed": evaluation["passed"]
    }


# ==========================================
# CONDITIONAL ROUTING
# ==========================================

def decide_next_step(state: LessonState):

    if state["passed"]:
        return "end"

    # Maximum 2 regeneration retries
    if state["attempts"] >= 2:
        return "end"

    return "regenerate"


# ==========================================
# REGENERATOR
# ==========================================

def regenerate_node(state: LessonState):

    lesson = regenerate_lesson(
        state["topic"],
        state["lesson"],
        state["feedback"]
    )

    return {
        "lesson": lesson,
        "attempts": state["attempts"] + 1
    }


# ==========================================
# BUILD LANGGRAPH
# ==========================================

workflow = StateGraph(LessonState)

workflow.add_node("generator", generate_node)
workflow.add_node("evaluator", evaluate_node)
workflow.add_node("regenerator", regenerate_node)

workflow.add_edge(START, "generator")

workflow.add_edge("generator", "evaluator")

workflow.add_conditional_edges(
    "evaluator",
    decide_next_step,
    {
        "end": END,
        "regenerate": "regenerator"
    }
)

workflow.add_edge("regenerator", "evaluator")

app = workflow.compile()


# ==========================================
# SAVE FINAL LESSON
# ==========================================

def save_lesson(result, topic):

    project_dir = os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))
    )

    output_dir = os.path.join(project_dir, "outputs")

    os.makedirs(output_dir, exist_ok=True)

    safe_topic = re.sub(
        r"[^a-zA-Z0-9_-]",
        "_",
        topic
    )

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    filename = f"{safe_topic}_{timestamp}.txt"

    filepath = os.path.join(output_dir, filename)

    with open(filepath, "w", encoding="utf-8") as file:

        file.write("FINAL GENERATED LESSON\n")
        file.write("=" * 50 + "\n\n")

        file.write(result["lesson"])

        file.write("\n\nFINAL EVALUATION\n")
        file.write("=" * 50 + "\n")

        file.write(f"Topic: {topic}\n")
        file.write(f"Score: {result['score']}\n")
        file.write(f"Passed: {result['passed']}\n")
        file.write(f"Retries: {result['attempts']}\n")
        file.write(f"Feedback: {result['feedback']}\n")

    print(f"\nLesson saved: {filepath}")

    return filepath


# ==========================================
# EXECUTE WORKFLOW
# ==========================================

def run_lesson_workflow(topic):

    initial_state = {
        "topic": topic,
        "lesson": "",
        "score": 0,
        "feedback": [],
        "attempts": 0,
        "passed": False
    }

    result = app.invoke(initial_state)

    # Save final run in persistent memory
    save_run(
        result["topic"],
        result["score"],
        result["passed"],
        result["attempts"],
        result["feedback"]
    )

    save_lesson(result, topic)

    return result


# ==========================================
# MAIN
# ==========================================

if __name__ == "__main__":

    topic = "Introduction to RAG"

    result = run_lesson_workflow(topic)

    print("\n========== FINAL EVALUATION ==========\n")

    print("Topic:", result["topic"])
    print("Score:", result["score"])
    print("Passed:", result["passed"])
    print("Retries:", result["attempts"])
    print("Feedback:", result["feedback"])