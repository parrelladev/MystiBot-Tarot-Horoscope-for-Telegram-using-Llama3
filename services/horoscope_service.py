import json
import requests
import re
from config.settings import LLM_API_URL, MODELO
from config.prompts import HOROSCOPE_PROMPT
from config.messages import ERROR_MESSAGES

def filter_llm_response(response_text):
    """
    Remove o conteúdo entre as tags <think> da resposta do LLM
    """
    # Remove todo o conteúdo entre as tags <think> e </think>
    filtered_text = re.sub(r'<think>.*?</think>', '', response_text, flags=re.DOTALL)
    # Remove linhas em branco extras
    filtered_text = re.sub(r'\n\s*\n', '\n\n', filtered_text)
    return filtered_text.strip()

def generate_response_horoscope(user_sign):
    """
    Gera uma resposta baseada no signo do usuário
    """
    prompt = HOROSCOPE_PROMPT.format(user_sign=user_sign)

    payload = {
        "role": "assistant",
        "model": MODELO,
        "prompt": prompt
    }

    try:
        response = requests.post(LLM_API_URL, json=payload)
        
        if response.status_code != 200:
            return ERROR_MESSAGES['llama_error']

        response_lines = response.text.strip().split('\n')
        concatenated_response = "".join([
            json.loads(line).get("response", "") for line in response_lines if "response" in json.loads(line)
        ]).strip()

        if not concatenated_response:
            return ERROR_MESSAGES['invalid_response']

        # Filtra a resposta para remover o conteúdo entre as tags <think>
        filtered_response = filter_llm_response(concatenated_response)

        # Formata a resposta final
        formatted_response = f"{filtered_response}"
        
        return formatted_response

    except Exception as e:
        return ERROR_MESSAGES['horoscope_error'].format(error=str(e)) 