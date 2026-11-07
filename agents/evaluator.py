def evaluate_lesson(lesson):

    score = 0
    feedback = []

    # Check 1: Correct definition of RAG
    if "retrieval-augmented generation" in lesson.lower():
        score += 40
    else:
        feedback.append(
            "Incorrect or missing definition of RAG"
        )

    # Check 2: Introduction
    if "introduction" in lesson.lower():
        score += 20
    else:
        feedback.append(
            "Introduction section is missing"
        )

    # Check 3: Examples
    if "example" in lesson.lower():
        score += 20
    else:
        feedback.append(
            "Practical examples are missing"
        )

    # Check 4: Conclusion
    if "conclusion" in lesson.lower():
        score += 20
    else:
        feedback.append(
            "Conclusion section is missing"
        )

    result = {
        "score": score,
        "passed": score >= 80,
        "feedback": feedback
    }

    return result