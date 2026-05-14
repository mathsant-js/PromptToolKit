# PromptToolKit

**Framework educacional para engenharia de prompts com LLMs** — comparação de técnicas de prompting, avaliação automática e geração de relatórios.

## Overview

O PromptToolKit é uma plataforma desenvolvida para estudo e experimentação de técnicas de Prompt Engineering utilizando modelos de linguagem (LLMs).

O projeto permite:

- Executar diferentes técnicas de prompting
- Comparar respostas entre técnicas
- Avaliar acurácia e consistência
- Testar temperatura de modelos
- Gerar gráficos e relatórios automáticos
- Trabalhar com tarefas modulares
- Integrar modelos locais via Ollama

## Funcionalidades

- **Zero-Shot Prompting**
- **Few-Shot Prompting**
- **Chain-of-Thought (CoT)**
- **Role Prompting**
- **Sistema modular de tarefas**
- **Templates reutilizáveis**
- **Exemplos Few-Shot externos**
- **Integração com Ollama**
- **Medição de tokens**
- **Análise de acurácia**
- **Teste de consistência**
- **Gráficos automáticos**
- **Exportação de resultados**

<br>
<br>

# Tecnologias Utilizadas

- Python 3.11+
- Pandas
- Matplotlib
- Ollama Python SDK
- python-dotenv

<br>
<br>

# Estrutura do Projeto

```bash
PromptToolKit/
├── data/
│   ├── inputs.json
│   └── examples.json
│
├── prompts/
│   ├── system_prompts.json
│   └── templates.json
│
├── src/
│   ├── evaluator.py
│   ├── llm_client.py
│   ├── prompt_builder.py
│   ├── report.py
│   ├── tasks.py
│   └── techniques.py
│
├── output/
│   ├── resultados.csv
│   └── graficos/
│
├── main.py
├── requirements.txt
└── .env.example
```

<br>
<br>

# Técnicas de Prompting

## Zero-Shot

Executa tarefas sem exemplos prévios.

## Few-Shot

Executa tarefas utilizando exemplos de entrada e saída.

## Chain-of-Thought

Força o modelo a raciocinar passo a passo.

## Role Prompting

Utiliza personas para alterar o comportamento do modelo.

<br>
<br>

# Tipos de Tarefas

O sistema já possui suporte para:

- Classificação
- Extração de informações
- Geração de texto
- Sumarização

Exemplos:

- Análise de sentimento
- Respostas automáticas
- Extração de JSON
- Resumos acadêmicos

<br>
<br>

# Instalação

## 1. Clonar o Repositório

```bash
git clone https://github.com/mathsant-js/PromptToolKit.git

cd PromptToolKit
```


## 2. Criar Ambiente Virtual

### Linux / Mac

```bash
python -m venv venv

source venv/bin/activate
```

### Windows

```bash
python -m venv venv

venv\Scripts\activate
```



## 3. Instalar Dependências

```bash
pip install -r requirements.txt
```

<br>
<br>

# Instalação do Ollama

O projeto utiliza Ollama para execução de modelos locais.

## Instalar Ollama

Site oficial:

```bash
https://ollama.com/download
```


## Iniciar o Ollama

```bash
ollama serve
```


## Baixar um Modelo

Exemplo utilizando Qwen:

```bash
ollama pull qwen2.5:1.5b
```

Você também pode utilizar:

- llama3
- mistral
- gemma
- deepseek
- phi3

<br>
<br>

# Configuração

## Criar arquivo `.env`

Crie um arquivo `.env` na raiz do projeto:

```env
OLLAMA_HOST=http://localhost:11434

MODEL_NAME=qwen2.5:1.5b
```

<br>
<br>

# Como Executar

## Executar o Projeto

```bash
python main.py
```


# Fluxo da Execução

O sistema irá:

1. Carregar tarefas
2. Carregar exemplos
3. Carregar templates
4. Executar todas as técnicas
5. Avaliar respostas
6. Gerar métricas
7. Gerar gráficos
8. Executar testes de temperatura

<br>
<br>

# Arquivos de Configuração

## `tasks.py`

Define todas as tarefas do sistema.

Exemplo:

```python
{
    "nome": "classificacao_feedback",
    "tipo": "classificacao",
    "instrucao": "Classifique o sentimento.",
    "template": "classificacao_template"
}
```



## `examples.json`

Armazena exemplos Few-Shot.

```json
{
  "classificacao_feedback": [
    {
      "input": "A plataforma é excelente.",
      "output": "POSITIVO"
    }
  ]
}
```


## `templates.json`

Define contexto e objetivo das tarefas.

```json
{
  "classificacao_template": {
    "contexto": "Especialista em sentimentos.",
    "objetivo": "Classificar feedbacks."
  }
}
```

<br>
<br>

# Relatórios Gerados

Após a execução:

```bash
output/
├── resultados.csv
└── graficos/
    ├── acuracia.png
    ├── custo.png
    ├── tempo_execucao.png
    └── temperatura.png
```

<br>
<br>

# Métricas Avaliadas

- Acurácia
- Tempo de resposta
- Quantidade de tokens
- Consistência
- Similaridade textual

<br>
<br>

# Exemplo de Execução

```bash
===================================
TAREFA: classificacao_feedback
===================================

[Zero-Shot]
Resposta: POSITIVO

[Few-Shot]
Resposta: POSITIVO

[Chain-of-Thought]
Resposta: POSITIVO

[Role Prompting]
Resposta: POSITIVO
```

<br>
<br>

# Personalização

Você pode facilmente:

- Adicionar novas tarefas
- Criar novas técnicas
- Integrar outros modelos
- Adicionar novas métricas
- Criar novos templates
- Adicionar novos datasets

<br>
<br>

# Modelos Compatíveis

Qualquer modelo suportado pelo Ollama:

- qwen2.5
- llama3
- mistral
- deepseek
- gemma
- phi3
- codellama

<br>
<br>

# Contribuição

Contribuições são bem-vindas.

## Como contribuir

1. Faça um fork
2. Crie uma branch

```bash
git checkout -b feature/nova-feature
```

3. Commit suas alterações

```bash
git commit -m "feat: nova feature"
```

4. Faça push

```bash
git push origin feature/nova-feature
```

5. Abra um Pull Request

<br>
<br>

# Licença

[MIT License](LICENSE)

<br>
<br>