from src.prompt_builder import (
    montar_prompt,
    adicionar_exemplos,
    adicionar_chain_of_thought
)


# ==========================================
# ZERO SHOT
# ==========================================

def zero_shot(
    tarefa,
    entrada,
    contexto,
    objetivo
):

    return montar_prompt(
        instrucao=tarefa["instrucao"],
        contexto=contexto,
        objetivo=objetivo,
        entrada=entrada,
        formato_output=tarefa["formato_output"]
    )


# ==========================================
# FEW SHOT
# ==========================================

def few_shot(
    tarefa,
    entrada,
    exemplos,
    contexto,
    objetivo
):

    prompt = montar_prompt(
        instrucao=tarefa["instrucao"],
        contexto=contexto,
        objetivo=objetivo,
        entrada=entrada,
        formato_output=tarefa["formato_output"]
    )

    return adicionar_exemplos(
        prompt,
        exemplos
    )


# ==========================================
# CHAIN OF THOUGHT
# ==========================================

def chain_of_thought(
    tarefa,
    entrada,
    passos,
    contexto,
    objetivo
):

    prompt = montar_prompt(
        instrucao=tarefa["instrucao"],
        contexto=contexto,
        objetivo=objetivo,
        entrada=entrada,
        formato_output=tarefa["formato_output"]
    )

    return adicionar_chain_of_thought(
        prompt,
        passos
    )


# ==========================================
# ROLE PROMPTING
# ==========================================

def role_prompting(
    tarefa,
    entrada,
    persona,
    contexto,
    objetivo
):

    prompt = montar_prompt(
        instrucao=tarefa["instrucao"],
        contexto=contexto,
        objetivo=objetivo,
        entrada=entrada,
        formato_output=tarefa["formato_output"]
    )

    return persona, prompt