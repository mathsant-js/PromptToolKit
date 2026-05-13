import tiktoken



def contar_tokens(texto):
    encoder = tiktoken.get_encoding("cl100k_base")
    return len(encoder.encode(texto))



def medir_acuracia(resposta, esperado):
    resposta = resposta.strip().upper()

    if resposta == esperado.upper():
        return 1

    return 0



def medir_consistencia(respostas):
    total = len(respostas)

    iguais = respostas.count(respostas[0])

    return round((iguais / total) * 100, 2)