from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="llama3.2",
    temperature=0
)


def regenerate_lesson(topic, lesson, feedback):

    prompt = f"""
    You are an expert educational content developer.

    Topic: {topic}

    Original Lesson:
    {lesson}

    Evaluator Feedback:
    {feedback}

    Instructions:
    1. Correct all identified mistakes.
    2. Explain concepts accurately.
    3. Include an introduction.
    4. Provide clear examples.
    5. Include a conclusion.
    6. Make the lesson beginner-friendly.

    Important:
    RAG means Retrieval-Augmented Generation.
    It retrieves relevant information from external
    sources and uses that information to generate
    accurate responses.

    Generate the improved lesson.
    """

    response = llm.invoke(prompt)

    return response.content