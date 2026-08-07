import httpx

from app.config.settings import settings
from app.core.exceptions import OpenRouterException
from app.core.logger import setup_logger

logger = setup_logger()


class OpenRouterClient:
    """
    Production OpenRouter Client
    """

    def __init__(self):
        self.base_url = settings.OPENROUTER_BASE_URL
        self.api_key = settings.OPENROUTER_API_KEY
        self.model = settings.OPENROUTER_MODEL

        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
            "HTTP-Referer": "http://localhost:8000",
            "X-Title": "Production RAG",
        }

    async def chat(
        self,
        prompt: str,
    ) -> str:

        payload = {
            "model": self.model,
            "messages": [
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
        }

        try:

            logger.info(f"Base URL : {self.base_url}")
            logger.info(f"Model : {self.model}")
            logger.info(
                f"Request URL : {self.base_url}/chat/completions"
            )

            async with httpx.AsyncClient(
                timeout=60,
            ) as client:

                response = await client.post(
                    f"{self.base_url}/chat/completions",
                    headers=self.headers,
                    json=payload,
                )

            logger.info(
                f"Status Code : {response.status_code}"
            )

            logger.info(
                f"Response : {response.text}"
            )

            response.raise_for_status()

            result = response.json()

            logger.info(
                "OpenRouter response received successfully."
            )

            return result["choices"][0]["message"]["content"]

        except Exception as e:

            logger.exception(
                "OpenRouter Error"
            )

            raise OpenRouterException(
                str(e)
            )