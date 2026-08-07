from app.services.prompt_builder import PromptBuilder

chunks = [
    {
        "document": "sample.pdf",
        "page": 1,
        "text": "The objective is to build a RAG application."
    },
    {
        "document": "sample.pdf",
        "page": 2,
        "text": "Use Qdrant for vector storage."
    }
]

prompt = PromptBuilder.build(
    question="What is the objective?",
    retrieved_chunks=chunks,
)

print(prompt)