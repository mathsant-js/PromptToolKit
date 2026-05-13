import json
import pandas as pd

from dotenv import load_dotenv

from src.tasks import TASKS

from src.techniques import (
    zero_shot,
    few_shot,
    chain_of_thought,
    role_prompting
)

from src.llm_client import LLMClient

from src.evaluator import (
    contar_tokens,
    medir_acuracia,
    medir_consistencia
)

from src.report import (
    gerar_tabela,
    grafico_acuracia,
    grafico_custo,
    grafico_tempo,
    grafico_temperatura,
    recomendar
)


# ==========================================
# CARREGAR CONFIGURAÇÕES
# ==========================================

load_dotenv()


# ==========================================
# FUNÇÃO AUXILIAR PARA CARREGAR JSON
# ==========================================

def carregar_json(caminho):

    with open(
        caminho,
        "r",
        encoding="utf-8"
    ) as arquivo:

        return json.load(arquivo)


# ==========================================
# CARREGAR DADOS
# ==========================================

inputs_data = carregar_json(
    "data/inputs.json"
)

examples_data = carregar_json(
    "data/examples.json"
)

personas = carregar_json(
    "prompts/system_prompts.json"
)

templates = carregar_json(
    "prompts/templates.json"
)


# ==========================================
# CLIENTE LLM
# ==========================================

client = LLMClient()


# ==========================================
# RESULTADOS
# ==========================================

resultados = []

resultados_temperatura = []


# ==========================================
# EXECUÇÃO PRINCIPAL
# ==========================================

for tarefa in TASKS:

    nome_tarefa = tarefa["nome"]

    print("\n===================================")
    print(f"TAREFA: {nome_tarefa}")
    print("===================================")

    # ======================================
    # DADOS DA TAREFA
    # ======================================

    inputs_tarefa = inputs_data.get(
        nome_tarefa,
        []
    )

    exemplos_tarefa = examples_data.get(
        nome_tarefa,
        []
    )

    template_nome = tarefa["template"]

    template = templates.get(
        template_nome,
        {}
    )

    contexto_template = template.get(
        "contexto",
        ""
    )

    objetivo_template = template.get(
        "objetivo",
        ""
    )

    passos_cot = tarefa.get(
        "passos_cot",
        []
    )

    # ======================================
    # PARA CADA INPUT
    # ======================================

    for item in inputs_tarefa:

        entrada = item["input"]

        esperado = item["esperado"]

        # ==================================
        # ZERO SHOT
        # ==================================

        tecnica = "Zero-Shot"

        prompt = zero_shot(
            tarefa=tarefa,
            entrada=entrada,
            contexto=contexto_template,
            objetivo=objetivo_template
        )

        resultado = client.chat(
            prompt=prompt
        )

        resposta = resultado.get(
            "resposta",
            ""
        )

        resultado_dict = {

            "tarefa":
            nome_tarefa,

            "tipo":
            tarefa["tipo"],

            "tecnica":
            tecnica,

            "input":
            entrada,

            "esperado":
            esperado,

            "resposta":
            resposta,

            "tokens_prompt":
            contar_tokens(prompt),

            "tempo_ms":
            resultado.get(
                "tempo_ms",
                0
            ),

            "acuracia":
            medir_acuracia(
                resposta,
                esperado
            )
        }

        resultados.append(
            resultado_dict
        )

        print(f"\n[{tecnica}]")
        print(f"Resposta: {resposta}")

        # ==================================
        # FEW SHOT
        # ==================================

        tecnica = "Few-Shot"

        prompt = few_shot(
            tarefa=tarefa,
            entrada=entrada,
            exemplos=exemplos_tarefa,
            contexto=contexto_template,
            objetivo=objetivo_template
        )

        resultado = client.chat(
            prompt=prompt
        )

        resposta = resultado.get(
            "resposta",
            ""
        )

        resultado_dict = {

            "tarefa":
            nome_tarefa,

            "tipo":
            tarefa["tipo"],

            "tecnica":
            tecnica,

            "input":
            entrada,

            "esperado":
            esperado,

            "resposta":
            resposta,

            "tokens_prompt":
            contar_tokens(prompt),

            "tempo_ms":
            resultado.get(
                "tempo_ms",
                0
            ),

            "acuracia":
            medir_acuracia(
                resposta,
                esperado
            )
        }

        resultados.append(
            resultado_dict
        )

        print(f"\n[{tecnica}]")
        print(f"Resposta: {resposta}")

        # ==================================
        # CHAIN OF THOUGHT
        # ==================================

        tecnica = "Chain-of-Thought"

        prompt = chain_of_thought(
            tarefa=tarefa,
            entrada=entrada,
            passos=passos_cot,
            contexto=contexto_template,
            objetivo=objetivo_template
        )

        resultado = client.chat(
            prompt=prompt
        )

        resposta = resultado.get(
            "resposta",
            ""
        )

        resultado_dict = {

            "tarefa":
            nome_tarefa,

            "tipo":
            tarefa["tipo"],

            "tecnica":
            tecnica,

            "input":
            entrada,

            "esperado":
            esperado,

            "resposta":
            resposta,

            "tokens_prompt":
            contar_tokens(prompt),

            "tempo_ms":
            resultado.get(
                "tempo_ms",
                0
            ),

            "acuracia":
            medir_acuracia(
                resposta,
                esperado
            )
        }

        resultados.append(
            resultado_dict
        )

        print(f"\n[{tecnica}]")
        print(f"Resposta: {resposta}")

        # ==================================
        # ROLE PROMPTING
        # ==================================

        tecnica = "Role Prompting"

        persona_nome = tarefa["persona"]

        persona = personas.get(
            persona_nome,
            ""
        )

        system, prompt = role_prompting(
            tarefa=tarefa,
            entrada=entrada,
            persona=persona,
            contexto=contexto_template,
            objetivo=objetivo_template
        )

        resultado = client.chat(
            prompt=prompt,
            system=system
        )

        resposta = resultado.get(
            "resposta",
            ""
        )

        resultado_dict = {

            "tarefa":
            nome_tarefa,

            "tipo":
            tarefa["tipo"],

            "tecnica":
            tecnica,

            "input":
            entrada,

            "esperado":
            esperado,

            "resposta":
            resposta,

            "tokens_prompt":
            contar_tokens(prompt),

            "tempo_ms":
            resultado.get(
                "tempo_ms",
                0
            ),

            "acuracia":
            medir_acuracia(
                resposta,
                esperado
            )
        }

        resultados.append(
            resultado_dict
        )

        print(f"\n[{tecnica}]")
        print(f"Resposta: {resposta}")


# ==========================================
# GERAR RELATÓRIOS
# ==========================================

print("\n===================================")
print("GERANDO RELATÓRIOS")
print("===================================")

df = gerar_tabela(
    resultados
)

grafico_acuracia(
    df
)

grafico_custo(
    df
)

grafico_tempo(
    df
)

recomendacoes = recomendar(
    df
)


# ==========================================
# TESTE DE TEMPERATURA
# ==========================================

print("\n===================================")
print("TESTE DE TEMPERATURA")
print("===================================")

temperaturas = [
    0.1,
    0.5,
    1.0
]

for recomendacao in recomendacoes:

    tarefa_nome = recomendacao["tarefa"]

    tecnica = recomendacao["melhor_tecnica"]

    tarefa = next(
        t for t in TASKS
        if t["nome"] == tarefa_nome
    )

    entrada = inputs_data[
        tarefa_nome
    ][0]["input"]

    exemplos_tarefa = examples_data.get(
        tarefa_nome,
        []
    )

    template_nome = tarefa["template"]

    template = templates.get(
        template_nome,
        {}
    )

    contexto_template = template.get(
        "contexto",
        ""
    )

    objetivo_template = template.get(
        "objetivo",
        ""
    )

    passos_cot = tarefa.get(
        "passos_cot",
        []
    )

    respostas = []

    for temp in temperaturas:

        # ==============================
        # ZERO SHOT
        # ==============================

        if tecnica == "Zero-Shot":

            prompt = zero_shot(
                tarefa=tarefa,
                entrada=entrada,
                contexto=contexto_template,
                objetivo=objetivo_template
            )

            resultado = client.chat(
                prompt=prompt,
                temp=temp
            )

        # ==============================
        # FEW SHOT
        # ==============================

        elif tecnica == "Few-Shot":

            prompt = few_shot(
                tarefa=tarefa,
                entrada=entrada,
                exemplos=exemplos_tarefa,
                contexto=contexto_template,
                objetivo=objetivo_template
            )

            resultado = client.chat(
                prompt=prompt,
                temp=temp
            )

        # ==============================
        # CHAIN OF THOUGHT
        # ==============================

        elif tecnica == "Chain-of-Thought":

            prompt = chain_of_thought(
                tarefa=tarefa,
                entrada=entrada,
                passos=passos_cot,
                contexto=contexto_template,
                objetivo=objetivo_template
            )

            resultado = client.chat(
                prompt=prompt,
                temp=temp
            )

        # ==============================
        # ROLE PROMPTING
        # ==============================

        else:

            persona_nome = tarefa["persona"]

            persona = personas.get(
                persona_nome,
                ""
            )

            system, prompt = role_prompting(
                tarefa=tarefa,
                entrada=entrada,
                persona=persona,
                contexto=contexto_template,
                objetivo=objetivo_template
            )

            resultado = client.chat(
                prompt=prompt,
                system=system,
                temp=temp
            )

        resposta = resultado.get(
            "resposta",
            ""
        )

        respostas.append(
            resposta
        )

        consistencia = medir_consistencia(
            respostas
        )

        resultado_temp = {

            "tarefa":
            tarefa_nome,

            "tecnica":
            tecnica,

            "temperatura":
            temp,

            "resposta":
            resposta,

            "consistencia":
            consistencia
        }

        resultados_temperatura.append(
            resultado_temp
        )

        print(f"\nTarefa: {tarefa_nome}")

        print(f"Técnica: {tecnica}")

        print(f"Temperatura: {temp}")

        print(f"Resposta: {resposta}")

        print(
            f"Consistência: {consistencia}%"
        )


# ==========================================
# GRÁFICO DE TEMPERATURA
# ==========================================

df_temp = pd.DataFrame(
    resultados_temperatura
)

grafico_temperatura(
    df_temp
)


# ==========================================
# FINAL
# ==========================================

print("\n===================================")

print("EXECUÇÃO FINALIZADA")

print("===================================")

print("\nArquivos gerados:")

print("- output/resultados.csv")

print("- output/graficos/acuracia.png")

print("- output/graficos/custo.png")

print("- output/graficos/tempo_execucao.png")

print("- output/graficos/temperatura.png")