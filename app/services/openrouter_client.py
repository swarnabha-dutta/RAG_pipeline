import httpx

from app.config.settings import settings
from app.core.exceptions import OpenRouterException
from app.core.logger import setup_logger

logger = setup_logger()


class OpenRouterClient:

    def __init__(self):
        self.base_url = settings.OPENROUTER_BASE_URL
        self.api_key = settings.OPENROUTER_API_KEY
        self.model = settings.OPENROUTER_MODEL

        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }

    async def chat(self, prompt: str):

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

            async with httpx.AsyncClient(timeout=60) as client:

                response = await client.post(
                    f"{self.base_url}/chat/completions",
                    headers=self.headers,
                    json=payload,
                )

            response.raise_for_status()

            result = response.json()

            return result["choices"][0]["message"]["content"]

        except Exception as e:
            logger.exception("OpenRouter Error")

            raise OpenRouterException(
                str(e)
            )