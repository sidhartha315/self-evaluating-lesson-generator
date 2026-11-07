from agents.generator import generate_lesson
from agents.evaluator import evaluate_lesson
from agents.regenerator import regenerate_lesson

# Project configuration
topic = "Introduction to RAG"
max_attempts = 3

# Step 1: Generate lesson
lesson = generate_lesson(topic)

for attempt in range(1, max_attempts + 1):

    print(f"\n========== ATTEMPT {attempt} ==========\n")

    print("GENERATED LESSON:\n")
    print(lesson)

    # Step 2: Evaluate lesson
    evaluation = evaluate_lesson(lesson)

    print("\n========== EVALUATION RESULT ==========\n")
    print("Score:", evaluation["score"])
    print("Passed:", evaluation["passed"])
    print("Feedback:", evaluation["feedback"])

    # Step 3: Check result
    if evaluation["passed"]:
        print("\nLesson successfully passed!")
        break

    # Step 4: Regenerate lesson
    if attempt < max_attempts:
        print("\nRegenerating lesson...")

        lesson = regenerate_lesson(
            topic,
            lesson,
            evaluation["feedback"]
        )

else:
    print("\nMaximum attempts reached.")