import tiktoken

# =====================================
# CONTAGEM DE TOKENS
# =====================================


def contar_tokens(texto):

    encoder = tiktoken.get_encoding("cl100k_base")

    return len(encoder.encode(texto))


# =====================================
# ACURÁCIA
# =====================================


def medir_acuracia(resposta, esperado):

    resposta = resposta.strip().upper()
    esperado = esperado.strip().upper()

    return int(resposta == esperado)


# =====================================
# CONSISTÊNCIA
# =====================================


def medir_consistencia(respostas):

    if not respostas:
        return 0

    primeira = respostas[0]

    iguais = respostas.count(primeira)

    consistencia = (iguais / len(respostas)) * 100

    return round(consistencia, 2)