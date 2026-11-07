from langchain_ollama import ChatOllama


def generate_lesson(topic):

    llm = ChatOllama(
        model="llama3.2",
        temperature=0.3
    )

    prompt = f"""
    You are an expert AI teacher.

    Create a beginner-friendly lesson about {topic}.
    IMPORTANT REQUIREMENTS:

1. Clearly define RAG as Retrieval-Augmented Generation.
2. Explain what RAG means in simple English.
3. Explain the three main steps:
   - Retrieval
   - Augmentation
   - Generation
4. Explain how RAG works step by step.
5. Give a practical real-world example.
6. Explain the advantages of RAG.
7. Include a separate Conclusion section.

IMPORTANT:
Never skip the full form of RAG.
Use the exact phrase "Retrieval-Augmented Generation".

    Target audience:
    Indian 12th-grade students with limited English vocabulary.

    Follow this structure:

    1. Introduction
    2. What is it?
    3. Why is it important?
    4. How does it work?
    5. Real-world example
    6. Advantages
    7. Summary

    Use simple English.
    Explain technical terms.
    Include practical examples.
    """

    response = llm.invoke(prompt)

    return response.content