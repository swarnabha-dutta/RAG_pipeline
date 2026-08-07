import re

from app.core.logger import setup_logger

logger = setup_logger()


class TextCleaner:
    """
    Production Text Cleaner

    Responsibilities
    ----------------
    - Remove unnecessary whitespace
    - Normalize line endings
    - Remove blank lines
    - Normalize tabs
    """

    @staticmethod
    def clean(text: str) -> str:
        """
        Clean extracted PDF text.

        Args:
            text: Raw extracted text

        Returns:
            Cleaned text
        """

        logger.info("Cleaning extracted text.")

        # Normalize line endings
        text = text.replace("\r\n", "\n")
        text = text.replace("\r", "\n")

        # Replace tabs with spaces
        text = text.replace("\t", " ")

        # Remove multiple spaces
        text = re.sub(r"[ ]{2,}", " ", text)

        # Remove multiple blank lines
        text = re.sub(r"\n{3,}", "\n\n", text)

        # Remove leading/trailing whitespace
        text = text.strip()

        logger.info("Text cleaned successfully.")

        return text