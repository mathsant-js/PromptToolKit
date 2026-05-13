def montar_prompt(
    instrucao,
    contexto,
    objetivo,
    entrada,
    formato_output
):

    return f"""
CONTEXTO:
{contexto}

OBJETIVO:
{objetivo}

INSTRUÇÃO:
{instrucao}

ENTRADA:
{entrada}

FORMATO DE SAÍDA:
{formato_output}
"""


def adicionar_exemplos(prompt, exemplos):

    bloco = "\n\nEXEMPLOS:\n"

    for exemplo in exemplos:

        bloco += (
            f"\nInput:\n{exemplo['input']}\n"
            f"Output:\n{exemplo['output']}\n"
        )

    return bloco + "\n" + prompt


def adicionar_chain_of_thought(prompt, passos):

    bloco = "\n\nPENSE PASSO A PASSO:\n"

    for i, passo in enumerate(passos, start=1):

        bloco += f"{i}. {passo}\n"

    return bloco + "\n" + prompt