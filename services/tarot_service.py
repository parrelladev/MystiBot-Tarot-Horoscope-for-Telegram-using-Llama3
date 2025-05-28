import random
import json
import requests
import re
from constants.tarot_cards import TAROT_CARDS
from config.settings import LLM_API_URL, MODELO
from config.prompts import TAROT_PROMPT
from config.messages import ERROR_MESSAGES

def generate_cards():
    """
    Gera 3 cartas aleatórias do Tarot
    """
    return random.sample(TAROT_CARDS, 3)

def filter_llm_response(response_text):
    """
    Remove o conteúdo entre as tags <think> da resposta do LLM
    """
    # Remove todo o conteúdo entre as tags <think> e </think>
    filtered_text = re.sub(r'<think>.*?</think>', '', response_text, flags=re.DOTALL)
    # Remove linhas em branco extras
    filtered_text = re.sub(r'\n\s*\n', '\n\n', filtered_text)
    return filtered_text.strip()

def generate_response(user_question, cards_message):
    """
    Gera uma resposta baseada na pergunta do usuário e nas cartas do Tarot
    """
    prompt = TAROT_PROMPT.format(
        cards_message=cards_message,
        user_question=user_question
    )

    payload = {
        "role": "assistant",
        "model": MODELO,
        "prompt": prompt
    }

    try:
        response = requests.post(LLM_API_URL, json=payload)
        response_lines = response.text.strip().split('\n')
        concatenated_response = "".join([json.loads(line)["response"] for line in response_lines if "response" in json.loads(line)])
        
        # Filtra a resposta para remover o conteúdo entre as tags <think>
        filtered_response = filter_llm_response(concatenated_response)
        
        # Formata a resposta final
        formatted_response = f"{filtered_response}"
        
        return formatted_response

    except Exception as e:
        return ERROR_MESSAGES['tarot_error'].format(error=str(e)) 