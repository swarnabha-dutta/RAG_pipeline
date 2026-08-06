class RAGException(Exception):
    """
    Base Exception for the application.
    """

    def __init__(self, message: str):
        self.message = message
        super().__init__(message)


class DocumentNotFoundException(RAGException):
    pass


class EmbeddingException(RAGException):
    pass


class QdrantException(RAGException):
    pass


class OpenRouterException(RAGException):
    pass