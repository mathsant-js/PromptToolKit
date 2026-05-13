def montar_prompt(instrucao, contexto, input_dados, formato_output):
    if not all([instrucao, contexto, input_dados, formato_output]):
        raise ValueError("Todos os campos devem ser preenchidos")

    prompt = f"""
INSTRUÇÃO:
{instrucao}

CONTEXTO:
{contexto}

DADOS:
{input_dados}

FORMATO DE SAÍDA:
{formato_output}
"""

    return prompt



def adicionar_exemplos(prompt, exemplos):
    bloco_exemplos = "\n\nEXEMPLOS:\n"

    for exemplo in exemplos:
        bloco_exemplos += (
            f"Input: {exemplo['input']}\n"
            f"Output: {exemplo['output']}\n\n"
        )

    return bloco_exemplos + prompt



def adicionar_cot(prompt, passos):
    bloco = "\n\nAnalise passo a passo:\n"

    for i, passo in enumerate(passos, start=1):
        bloco += f"{i}. {passo}\n"

    return bloco + prompt