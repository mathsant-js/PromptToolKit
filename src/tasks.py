TASKS = [

    {
        "nome": "classificacao_feedback",

        "tipo": "classificacao",

        "instrucao":
        "Classifique o sentimento do feedback do aluno.",

        "formato_output":
        "Responda apenas POSITIVO, NEGATIVO, MISTO ou NEUTRO.",

        "exemplos_fewshot": [

            {
                "input":
                "A plataforma é excelente e os professores explicam muito bem.",

                "output":
                "POSITIVO"
            },

            {
                "input":
                "As aulas travam constantemente e o suporte não responde.",

                "output":
                "NEGATIVO"
            }
        ],

        "passos_cot": [

            "Identifique pontos positivos",

            "Identifique pontos negativos",

            "Determine o sentimento predominante"
        ],

        "persona":
        "coordenador_pedagogico"
    },



    {
        "nome": "extracao_informacoes_curso",

        "tipo": "extracao",

        "instrucao":
        "Extraia as informações acadêmicas relevantes do texto.",

        "formato_output":
        "Retorne um JSON estruturado.",

        "exemplos_fewshot": [

            {
                "input":
                "Curso de Python Avançado com carga horária de 40 horas.",

                "output":
                "{curso: Python Avançado, carga_horaria: 40 horas}"
            }
        ],

        "passos_cot": [

            "Identifique o nome do curso",

            "Identifique carga horária",

            "Monte o JSON estruturado"
        ],

        "persona":
        "assistente_academico"
    },



    {
        "nome": "geracao_resposta_aluno",

        "tipo": "geracao",

        "instrucao":
        "Gere uma resposta profissional e acolhedora para o aluno.",

        "formato_output":
        "Resposta educada, clara e objetiva.",

        "exemplos_fewshot": [

            {
                "input":
                "Não consegui acessar minha atividade.",

                "output":
                "Vamos ajudá-lo a resolver o acesso à atividade."
            }
        ],

        "passos_cot": [

            "Identifique o problema do aluno",

            "Demonstre empatia",

            "Apresente uma solução clara"
        ],

        "persona":
        "tutor_virtual"
    }
]