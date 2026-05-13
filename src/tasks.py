TASKS = [

    {
        "nome": "classificacao_feedback",

        "descricao":
        "Classificação de sentimento de feedbacks educacionais.",

        "tipo": "classificacao",

        "instrucao":
        "Classifique o sentimento do feedback do aluno.",

        "formato_output":
        "Responda apenas POSITIVO, NEGATIVO, MISTO ou NEUTRO.",

        "template":
        "classificacao_template",

        "metricas":
        ["acuracia"],

        "persona":
        "coordenador_pedagogico"
    },



    {
        "nome": "extracao_informacoes_curso",

        "descricao":
        "Extração de informações acadêmicas estruturadas.",

        "tipo": "extracao",

        "instrucao":
        "Extraia as informações acadêmicas relevantes do texto.",

        "formato_output":
        "Retorne um JSON válido.",

        "template":
        "extracao_template",

        "metricas":
        ["acuracia", "json_valido"],

        "persona":
        "assistente_academico"
    },



    {
        "nome": "geracao_resposta_aluno",

        "descricao":
        "Geração de respostas empáticas para alunos.",

        "tipo": "geracao",

        "instrucao":
        "Gere uma resposta profissional e acolhedora para o aluno.",

        "formato_output":
        "Resposta educada, clara e objetiva.",

        "template":
        "geracao_template",

        "metricas":
        ["similaridade"],

        "persona":
        "tutor_virtual"
    },



    {
        "nome": "sumarizacao_conteudo",

        "descricao":
        "Resumo acadêmico de conteúdos educacionais.",

        "tipo": "sumarizacao",

        "instrucao":
        "Resuma o conteúdo acadêmico apresentado.",

        "formato_output":
        "Retorne bullet points objetivos.",

        "template":
        "sumarizacao_template",

        "metricas":
        ["similaridade"],

        "persona":
        "especialista_resumos"
    }
]