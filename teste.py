from src.llm_client import LLMClient

client = LLMClient()

resultado = client.chat(
    prompt="Diga ola",
    system="Você é um assistente útil."
)

print(resultado)