from langchain_ollama import ChatOllama


def generate_lesson(topic, learning_notes=None):

    llm = ChatOllama(
        model="llama3.2",
        temperature=0.3
    )

    prompt = f"""
    You are an expert AI teacher.

    Create a beginner-friendly lesson about {topic}.

    Target audience:
    Indian 12th-grade students with limited English vocabulary.

    Follow this structure:

    1. Introduction
    2. What is RAG?
    3. Why is RAG important?
    4. How does RAG work?
    5. Practical Example
    6. Advantages
    7. Conclusion

    Requirements:

    - Define RAG as Retrieval-Augmented Generation.
    - Explain the meaning in simple English.
    - Explain Retrieval, Augmentation and Generation.
    - Explain the process step by step.
    - Explain embeddings, vectors and language models.
    - Use simple sentences.
    - Include a practical real-world example.
    - Include a sample user question and generated answer.
    - Do not skip any section.

    Previous evaluation feedback:
    {learning_notes}

    Learn from previous failures.
    Avoid repeating previously identified mistakes.

    Generate the complete lesson.
    """

    response = llm.invoke(prompt)

    return response.content