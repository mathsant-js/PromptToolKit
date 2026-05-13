import os
import requests
import time
from dotenv import load_dotenv

load_dotenv()


class LLMClient:
    def __init__(self):
        self.host = os.getenv("OLLAMA_HOST")
        self.model = os.getenv("MODEL_NAME")

    def chat(self, prompt, system="", temp=0.5, max_tokens=300):
        url = f"{self.host}/api/chat"

        payload = {
            "model": self.model,
            "messages": [
                {
                    "role": "system",
                    "content": system
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            "options": {
                "temperature": temp,
                "num_predict": max_tokens
            },
            "stream": False
        }

        inicio = time.time()

        try:
            response = requests.post(url, json=payload, timeout=120)
            response.raise_for_status()

            data = response.json()

            tempo_ms = round((time.time() - inicio) * 1000, 2)

            resposta = data["message"]["content"]

            return {
                "resposta": resposta,
                "tempo_ms": tempo_ms
            }

        except requests.exceptions.RequestException as erro:
            return {
                "erro": str(erro)
            }