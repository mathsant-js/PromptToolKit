import json

from src.llm_client import LLMClient
from src.techniques import role_prompting
from src.tasks import TASKS


# carregar personas
with open("prompts/system_prompts.json", "r", encoding="utf-8") as arquivo:
    personas = json.load(arquivo)


client = LLMClient()

# pegar primeira tarefa
tarefa = TASKS[0]

entrada = """
Comprei o produto semana passada.
Ele veio quebrado e o suporte demorou muito para responder.
Estou extremamente frustrado.
"""

# carregar persona da tarefa
persona_nome = tarefa["persona"]

persona = personas[persona_nome]

# gerar prompt
system, prompt = role_prompting(
    tarefa,
    entrada,
    persona
)

print("========== SYSTEM ==========")
print(system)

print("========== PERSONA ==========")
print(persona_nome)


print("\n========== PROMPT ==========")
print(prompt)

print("\n========== RESPOSTA ==========")

resultado = client.chat(
    prompt=prompt,
    system=system,
    temp=0.5
)

print(resultado["resposta"])