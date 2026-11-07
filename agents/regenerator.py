from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="llama3.2",
    temperature=0
)


def regenerate_lesson(topic, lesson, feedback):

    prompt = f"""
    You are an expert educational content developer.

    Topic: {topic}

    Previous Lesson:
    {lesson}

    Evaluator Feedback:
    {feedback}

    Your task:
    Regenerate the complete lesson and fix EVERY issue
    mentioned in the evaluator feedback.

    Requirements:
    1. Explain the topic accurately.
    2. Include a clear introduction.
    3. Explain why the topic is useful.
    4. Explain how the concept works step by step.
    5. Explain technical terms in beginner-friendly language.
    6. Include a practical real-world example.
    7. Include all important concepts.
    8. End with a conclusion or summary.

    Important:
    - Do not ignore any evaluator feedback.
    - Do not simply repeat the previous lesson.
    - Do not include unsupported information.
    - Return the complete improved lesson.
    """

    response = llm.invoke(prompt)

    return response.content