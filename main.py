from src.tasks import TASKS
from src.techniques import (
    zero_shot,
    few_shot,
    chain_of_thought,
    role_prompting
)
from src.llm_client import LLMClient


client = LLMClient()


for tarefa in TASKS:
    print(f"Executando tarefa: {tarefa['nome']}")