from app.core.logger import setup_logger

logger = setup_logger()


class PromptBuilder:
    """
    Production Prompt Builder

    Responsibilities
    ----------------
    - Build production-ready prompt
    - Inject retrieved context
    - Prevent hallucinations
    - Force citation-aware responses
    """

    @staticmethod
    def build(
        question: str,
        retrieved_chunks: list[dict],
    ) -> str:
        """
        Build prompt for the LLM.

        Parameters
        ----------
        question : str
            User question

        retrieved_chunks : list[dict]
            Retrieved chunks from Qdrant

        Returns
        -------
        str
            Final prompt
        """

        logger.info("Building RAG prompt.")

        context = ""

        for index, chunk in enumerate(
            retrieved_chunks,
            start=1,
        ):

            context += (
                f"Context {index}\n"
                f"Document: {chunk['document']}\n"
                f"Page: {chunk['page']}\n"
                f"Content:\n"
                f"{chunk['text']}\n\n"
            )

        prompt = f"""
You are a production Retrieval-Augmented Generation (RAG) assistant.

Answer ONLY using the provided context.

Rules:
1. Do NOT use external knowledge.
2. Do NOT hallucinate.
3. If the answer is not found in the context, reply:
   "The requested information is not available in the supplied documents."
4. Give a concise and accurate answer.
5. Preserve important technical terminology.
6. At the end of your answer include the supporting sources.

Context:
{context}

Question:
{question}

Response Format

Answer:
<answer>

Sources:

- Document:
- Page:
"""

        logger.info("Prompt created successfully.")

        return prompt.strip()