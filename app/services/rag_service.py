from app.core.logger import setup_logger
from app.services.openrouter_client import OpenRouterClient
from app.services.prompt_builder import PromptBuilder
from app.services.retrieval_service import RetrievalService

logger = setup_logger()


class RAGService:
    """
    Production RAG Service

    Responsibilities
    ----------------
    - Retrieve relevant chunks
    - Build prompt
    - Generate final answer
    """

    def __init__(self):
        self.retrieval_service = RetrievalService()
        self.prompt_builder = PromptBuilder()
        self.llm = OpenRouterClient()

    async def answer_question(
        self,
        question: str,
    ) -> dict:
        """
        Complete RAG pipeline.

        Returns
        -------
        {
            answer,
            citations
        }
        """

        logger.info(
            f"Processing question: {question}"
        )

        # Retrieve context
        chunks = self.retrieval_service.retrieve(
            question=question,
        )

        # Build prompt
        prompt = self.prompt_builder.build(
            question=question,
            retrieved_chunks=chunks,
        )

        # Generate answer
        answer = await self.llm.chat(
            prompt
        )

        logger.info(
            "Answer generated successfully."
        )

        citations = []

        for chunk in chunks:

            citations.append(
                {
                    "document": chunk["document"],
                    "page": chunk["page"],
                    "text": chunk["text"],
                }
            )

        return {
            "answer": answer,
            "citations": citations,
        }