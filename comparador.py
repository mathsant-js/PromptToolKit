import json
import time

from src.llm_client import LLMClient

from src.techniques import (
    zero_shot,
    few_shot,
    chain_of_thought,
    role_prompting
)

from src.tasks import TASKS


# =========================
# CARREGAR PERSONAS
# =========================

with open(
    "prompts/system_prompts.json",
    "r",
    encoding="utf-8"
) as arquivo:

    personas = json.load(arquivo)


# =========================
# INICIAR CLIENTE
# =========================

client = LLMClient()


# =========================
# INPUT DE TESTE
# =========================

entrada = """
O notebook chegou funcionando,
mas após 3 dias começou a desligar sozinho.

O suporte pediu 7 dias úteis para análise
e ainda não obtive retorno.
"""


# =========================
# PEGAR TAREFA
# =========================

tarefa = TASKS[0]


# =========================
# LISTA DE TÉCNICAS
# =========================

tecnicas = [
    "Zero-Shot",
    "Few-Shot",
    "Chain-of-Thought",
    "Role Prompting"
]


# =========================
# ZERO SHOT
# =========================

print("\n==============================")
print("TESTANDO ZERO-SHOT")
print("==============================")

prompt = zero_shot(
    tarefa,
    entrada
)

inicio = time.time()

resultado = client.chat(
    prompt=prompt
)

fim = time.time()

print("\nPROMPT:\n")
print(prompt)

print("\nRESPOSTA:\n")
print(resultado["resposta"])

print(f"\nTempo: {round(fim - inicio, 2)} segundos")


# =========================
# FEW SHOT
# =========================

print("\n==============================")
print("TESTANDO FEW-SHOT")
print("==============================")

prompt = few_shot(
    tarefa,
    entrada,
    tarefa["exemplos_fewshot"]
)

inicio = time.time()

resultado = client.chat(
    prompt=prompt
)

fim = time.time()

print("\nPROMPT:\n")
print(prompt)

print("\nRESPOSTA:\n")
print(resultado["resposta"])

print(f"\nTempo: {round(fim - inicio, 2)} segundos")


# =========================
# CHAIN OF THOUGHT
# =========================

print("\n==============================")
print("TESTANDO CHAIN-OF-THOUGHT")
print("==============================")

prompt = chain_of_thought(
    tarefa,
    entrada,
    tarefa["passos_cot"]
)

inicio = time.time()

resultado = client.chat(
    prompt=prompt
)

fim = time.time()

print("\nPROMPT:\n")
print(prompt)

print("\nRESPOSTA:\n")
print(resultado["resposta"])

print(f"\nTempo: {round(fim - inicio, 2)} segundos")


# =========================
# ROLE PROMPTING
# =========================

print("\n==============================")
print("TESTANDO ROLE PROMPTING")
print("==============================")

persona_nome = tarefa["persona"]

persona = personas[persona_nome]

system, prompt = role_prompting(
    tarefa,
    entrada,
    persona
)

inicio = time.time()

resultado = client.chat(
    prompt=prompt,
    system=system
)

fim = time.time()

print("\nSYSTEM:\n")
print(system)

print("\nPROMPT:\n")
print(prompt)

print("\nRESPOSTA:\n")
print(resultado["resposta"])

print(f"\nTempo: {round(fim - inicio, 2)} segundos")


# =========================
# FINAL
# =========================

print("\n==============================")
print("COMPARAÇÃO FINALIZADA")
print("==============================")