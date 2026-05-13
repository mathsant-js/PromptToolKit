import pandas as pd
import matplotlib.pyplot as plt



def gerar_tabela(resultados):
    df = pd.DataFrame(resultados)

    df.to_csv("output/resultados.csv", index=False)

    print(df)

    return df



def grafico_acuracia(df):
    media = df.groupby("tecnica")["acuracia"].mean()

    media.plot(kind="bar")

    plt.title("Acurácia por Técnica")

    plt.savefig("output/graficos/acuracia.png")

    plt.close()



def grafico_custo(df):
    media = df.groupby("tecnica")["tokens"].mean()

    media.plot(kind="bar")

    plt.title("Custo Médio de Tokens")

    plt.savefig("output/graficos/custo.png")

    plt.close()