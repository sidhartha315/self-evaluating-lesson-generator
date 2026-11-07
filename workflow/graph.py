import os
import re
from datetime import datetime
from typing import TypedDict

from langgraph.graph import StateGraph, START, END

from agents.generator import generate_lesson
from agents.evaluator import evaluate_lesson
from agents.regenerator import regenerate_lesson


# ==========================================
# STEP 1: DEFINE WORKFLOW STATE
# ==========================================

class LessonState(TypedDict):
    topic: str
    lesson: str
    score: int
    feedback: list
    attempts: int
    passed: bool


# ==========================================
# STEP 2: GENERATOR NODE
# ==========================================

def generate_node(state: LessonState):

    lesson = generate_lesson(state["topic"])

    return {
        "lesson": lesson,
        "attempts": 0
    }


# ==========================================
# STEP 3: EVALUATOR NODE
# ==========================================

def evaluate_node(state: LessonState):

    evaluation = evaluate_lesson(state["lesson"])

    return {
        "score": evaluation["score"],
        "feedback": evaluation["feedback"],
        "passed": evaluation["passed"]
    }


# ==========================================
# STEP 4: CONDITIONAL ROUTING
# ==========================================

def decide_next_step(state: LessonState):

    if state["passed"]:
        return "end"

    if state["attempts"] >= 3:
        return "end"

    return "regenerate"


# ==========================================
# STEP 5: REGENERATOR NODE
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
# STEP 6: BUILD LANGGRAPH WORKFLOW
# ==========================================

workflow = StateGraph(LessonState)


# Register nodes

workflow.add_node("generator", generate_node)
workflow.add_node("evaluator", evaluate_node)
workflow.add_node("regenerator", regenerate_node)


# Connect nodes

workflow.add_edge(START, "generator")

workflow.add_edge("generator", "evaluator")


# Conditional routing

workflow.add_conditional_edges(
    "evaluator",
    decide_next_step,
    {
        "end": END,
        "regenerate": "regenerator"
    }
)

workflow.add_edge("regenerator", "evaluator")


# ==========================================
# STEP 7: COMPILE WORKFLOW
# ==========================================

app = workflow.compile()


# ==========================================
# STEP 8: SAVE GENERATED LESSON
# ==========================================

def save_lesson(result, topic):

    # Get project root directory
    project_dir = os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))
    )

    # Create outputs folder
    output_dir = os.path.join(project_dir, "outputs")

    os.makedirs(output_dir, exist_ok=True)

    # Clean topic for filename
    safe_topic = re.sub(
        r"[^a-zA-Z0-9_-]",
        "_",
        topic
    )

    timestamp = datetime.now().strftime(
        "%Y%m%d_%H%M%S"
    )

    filename = f"{safe_topic}_{timestamp}.txt"

    filepath = os.path.join(output_dir, filename)

    # Write lesson and evaluation
    with open(filepath, "w", encoding="utf-8") as file:

        file.write("GENERATED LESSON\n")
        file.write("=" * 50 + "\n\n")

        file.write(result["lesson"])

        file.write("\n\nFINAL EVALUATION\n")
        file.write("=" * 50 + "\n\n")

        file.write(f"Topic: {topic}\n")
        file.write(f"Score: {result['score']}\n")
        file.write(f"Passed: {result['passed']}\n")
        file.write(f"Attempts: {result['attempts']}\n")
        file.write(f"Feedback: {result['feedback']}\n")

    print(f"\nLesson saved successfully: {filepath}")

    return filepath


# ==========================================
# STEP 9: EXECUTE WORKFLOW
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

    # Execute LangGraph
    result = app.invoke(initial_state)

    # Save generated lesson
    save_lesson(result, topic)

    return result


# ==========================================
# STEP 10: MAIN EXECUTION
# ==========================================

if __name__ == "__main__":

    topic = "Introduction to RAG"

    result = run_lesson_workflow(topic)

    print("\n========== FINAL LESSON ==========\n")

    print(result["lesson"])

    print("\n========== FINAL EVALUATION ==========\n")

    print("Topic:", result["topic"])
    print("Score:", result["score"])
    print("Passed:", result["passed"])
    print("Attempts:", result["attempts"])
    print("Feedback:", result["feedback"])