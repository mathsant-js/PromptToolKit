from src.prompt_builder import (
    montar_prompt,
    adicionar_exemplos,
    adicionar_cot
)



def zero_shot(tarefa, entrada):
    return montar_prompt(
        tarefa["instrucao"],
        "Atendimento ao cliente",
        entrada,
        tarefa["formato_output"]
    )



def few_shot(tarefa, entrada, exemplos):
    prompt = montar_prompt(
        tarefa["instrucao"],
        "Atendimento ao cliente",
        entrada,
        tarefa["formato_output"]
    )

    return adicionar_exemplos(prompt, exemplos)



def chain_of_thought(tarefa, entrada, passos):
    prompt = montar_prompt(
        tarefa["instrucao"],
        "Atendimento ao cliente",
        entrada,
        tarefa["formato_output"]
    )

    return adicionar_cot(prompt, passos)



def role_prompting(tarefa, entrada, persona):
    prompt = montar_prompt(
        tarefa["instrucao"],
        "Atendimento ao cliente",
        entrada,
        tarefa["formato_output"]
    )

    return persona, prompt