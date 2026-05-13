TASKS = [
    {
        "tipo": "classificacao",
        "instrucao": "Classifique o sentimento do cliente.",
        "formato_output": "Responda apenas POSITIVO, NEGATIVO, MISTO ou NEUTRO.",
        "exemplos_fewshot": [
            {
                "input": "Adorei o atendimento",
                "output": "POSITIVO"
            },
            {
                "input": "Produto chegou quebrado",
                "output": "NEGATIVO"
            }
        ],
        "passos_cot": [
            "Identifique aspectos positivos",
            "Identifique aspectos negativos",
            "Determine o sentimento predominante"
        ],
        "persona": "analista_cx"
    },

    {
        "nome": "extracao_dados",
        "tipo": "extracao",
        "instrucao": "Extraia os dados relevantes do texto.",
        "formato_output": "Retorne um JSON estruturado.",
        "exemplos_fewshot": [
            {
                "input": "Notebook Dell de R$3500 com defeito",
                "output": "{produto: Notebook Dell, preco: R$3500}"
            }
        ],
        "passos_cot": [
            "Identifique produto",
            "Identifique valores",
            "Monte o JSON"
        ],
        "persona": "especialista_suporte"
    },

    {
        "nome": "geracao_resposta",
        "tipo": "geracao",
        "instrucao": "Gere uma resposta profissional para o cliente.",
        "formato_output": "Resposta cordial e objetiva.",
        "exemplos_fewshot": [
            {
                "input": "Meu pedido atrasou",
                "output": "Pedimos desculpas pelo atraso."
            }
        ],
        "passos_cot": [
            "Identifique o problema",
            "Mostre empatia",
            "Apresente solução"
        ],
        "persona": "analista_cx"
    }
]