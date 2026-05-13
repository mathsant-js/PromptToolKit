import os

import pandas as pd
import matplotlib.pyplot as plt


# ==========================================
# GARANTIR PASTAS
# ==========================================

os.makedirs(
    "output/graficos",
    exist_ok=True
)


# ==========================================
# GERAR TABELA CSV
# ==========================================

def gerar_tabela(resultados):

    df = pd.DataFrame(resultados)

    caminho_csv = "output/resultados.csv"

    df.to_csv(
        caminho_csv,
        index=False,
        encoding="utf-8"
    )

    print("\n===================================")
    print("TABELA DE RESULTADOS")
    print("===================================")

    print(df)

    print(f"\nCSV salvo em: {caminho_csv}")

    return df


# ==========================================
# GRÁFICO DE ACURÁCIA
# ==========================================

def grafico_acuracia(df):

    media = (
        df.groupby("tecnica")["acuracia"]
        .mean()
        .sort_values(ascending=False)
    )

    plt.figure(figsize=(8, 5))

    media.plot(kind="bar")

    plt.title("Acurácia Média por Técnica")

    plt.xlabel("Técnica")

    plt.ylabel("Acurácia Média")

    plt.tight_layout()

    caminho = (
        "output/graficos/acuracia.png"
    )

    plt.savefig(caminho)

    plt.close()

    print(
        f"\nGráfico salvo: {caminho}"
    )


# ==========================================
# GRÁFICO DE CUSTO
# ==========================================

def grafico_custo(df):

    media = (
        df.groupby("tecnica")[
            "tokens_prompt"
        ]
        .mean()
        .sort_values()
    )

    plt.figure(figsize=(8, 5))

    media.plot(kind="bar")

    plt.title(
        "Custo Médio de Tokens"
    )

    plt.xlabel("Técnica")

    plt.ylabel(
        "Tokens Médios"
    )

    plt.tight_layout()

    caminho = (
        "output/graficos/custo.png"
    )

    plt.savefig(caminho)

    plt.close()

    print(
        f"\nGráfico salvo: {caminho}"
    )


# ==========================================
# GRÁFICO DE TEMPO
# ==========================================

def grafico_tempo(df):

    media = (
        df.groupby("tecnica")[
            "tempo_ms"
        ]
        .mean()
        .sort_values()
    )

    plt.figure(figsize=(8, 5))

    media.plot(kind="bar")

    plt.title(
        "Tempo Médio de Execução"
    )

    plt.xlabel("Técnica")

    plt.ylabel("Tempo Médio (ms)")

    plt.tight_layout()

    caminho = (
        "output/graficos/tempo_execucao.png"
    )

    plt.savefig(caminho)

    plt.close()

    print(
        f"\nGráfico salvo: {caminho}"
    )


# ==========================================
# GRÁFICO DE TEMPERATURA
# ==========================================

def grafico_temperatura(df_temp):

    media = (
        df_temp.groupby("temperatura")[
            "consistencia"
        ]
        .mean()
        .sort_index()
    )

    plt.figure(figsize=(8, 5))

    media.plot(
        kind="line",
        marker="o"
    )

    plt.title(
        "Consistência por Temperatura"
    )

    plt.xlabel("Temperatura")

    plt.ylabel(
        "Consistência Média (%)"
    )

    plt.grid(True)

    plt.tight_layout()

    caminho = (
        "output/graficos/temperatura.png"
    )

    plt.savefig(caminho)

    plt.close()

    print(
        f"\nGráfico salvo: {caminho}"
    )


# ==========================================
# RECOMENDAÇÃO AUTOMÁTICA
# ==========================================

def recomendar(df):

    print("\n===================================")
    print("RECOMENDAÇÕES")
    print("===================================")

    recomendacoes = []

    tarefas = df["tarefa"].unique()

    for tarefa in tarefas:

        df_tarefa = df[
            df["tarefa"] == tarefa
        ]

        melhor = (
            df_tarefa.sort_values(
                by=[
                    "acuracia",
                    "tokens_prompt"
                ],
                ascending=[
                    False,
                    True
                ]
            )
            .iloc[0]
        )

        recomendacao = {
            "tarefa": tarefa,
            "melhor_tecnica":
                melhor["tecnica"],
            "acuracia":
                melhor["acuracia"],
            "tokens":
                melhor["tokens_prompt"]
        }

        recomendacoes.append(
            recomendacao
        )

        print(f"\nTarefa: {tarefa}")

        print(
            f"Melhor Técnica: "
            f"{melhor['tecnica']}"
        )

        print(
            f"Acurácia: "
            f"{melhor['acuracia']}"
        )

        print(
            f"Tokens: "
            f"{melhor['tokens_prompt']}"
        )

    return recomendacoes