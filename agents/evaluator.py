def evaluate_lesson(lesson):
    """
    Evaluates a generated lesson using a strict checklist.
    Every criterion must pass for the lesson to pass.
    """

    feedback = []
    lesson_lower = lesson.lower()

    # 1. Correct definition of RAG
    definition_keywords = [
        "retrieval-augmented generation",
        "rag"
    ]

    if all(word in lesson_lower for word in definition_keywords):
        pass
    else:
        feedback.append(
            "Missing or incorrect definition of RAG. Explain Retrieval-Augmented Generation."
        )

    # 2. Introduction and purpose
    if "introduction" in lesson_lower and (
        "why" in lesson_lower or "purpose" in lesson_lower
    ):
        pass
    else:
        feedback.append(
            "Introduction or explanation of why RAG is useful is missing."
        )

    # 3. How RAG works
    how_keywords = [
        "how",
        "retrieval",
        "generation",
        "document"
    ]

    if all(word in lesson_lower for word in how_keywords):
        pass
    else:
        feedback.append(
            "Explanation of how RAG works is incomplete."
        )

    # 4. Practical example
    if "example" in lesson_lower and (
        "question" in lesson_lower or "answer" in lesson_lower
    ):
        pass
    else:
        feedback.append(
            "A practical beginner-friendly example is missing."
        )

    # 5. Important RAG concepts
    concept_keywords = [
        "embedding",
        "vector",
        "language model"
    ]

    missing_concepts = [
        word for word in concept_keywords
        if word not in lesson_lower
    ]

    if not missing_concepts:
        pass
    else:
        feedback.append(
            "Important RAG concepts are missing: "
            + ", ".join(missing_concepts)
        )

    # 6. Conclusion
    if "conclusion" in lesson_lower or "summary" in lesson_lower:
        pass
    else:
        feedback.append(
            "Conclusion or summary section is missing."
        )

    # Strict evaluation: all six criteria must pass
    total_checks = 6
    passed_checks = total_checks - len(feedback)

    score = int((passed_checks / total_checks) * 100)

    result = {
        "score": score,
        "passed": len(feedback) == 0,
        "feedback": feedback
    }

    return result