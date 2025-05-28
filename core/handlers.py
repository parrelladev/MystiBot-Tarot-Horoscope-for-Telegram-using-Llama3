import telebot
from constants.tarot_cards import ZODIAC_SIGNS
from services.tarot_service import generate_cards, generate_response
from services.horoscope_service import generate_response_horoscope
from utils.keyboards import get_main_keyboard, get_zodiac_keyboard

def handle_start(message, bot):
    """
    Manipula o comando /start
    """
    bot.send_message(message.chat.id, "🧙‍♀️ Olá! Eu sou o consultor MystiBot.\n\nSelecione uma das opções abaixo para começar:", reply_markup=get_main_keyboard())

def handle_tarot(message, bot):
    """
    Inicia a leitura das cartas do Tarot
    """
    sent = bot.reply_to(message, "🗯️ Por favor, digite a pergunta que você deseja fazer ao Tarot e espere eu fazer a leitura das cartas.")
    bot.register_next_step_handler(sent, lambda m: process_tarot_question(m, bot))

def handle_horoscope(message, bot):
    """
    Inicia a leitura do horóscopo
    """
    bot.send_message(message.chat.id, "Por favor, escolha um signo do zodíaco abaixo:", reply_markup=get_zodiac_keyboard())
    bot.register_next_step_handler(message, lambda m: process_horoscope_question(m, bot))

def handle_info(message, bot):
    """
    Fornece informações sobre o funcionamento do bot
    """
    bot.send_message(message.chat.id, "Eu sou um bot que oferece leituras de tarô e horóscopo. Utilizando a API Llama 3.1, meu objetivo é oferecer insights e orientações sobre questões pessoais, profissionais e espirituais por meio de uma interação misticas e milenares.")

def handle_about(message, bot):
    """
    Fornece informações sobre Tarot e horóscopos
    """
    bot.send_message(message.chat.id, "O Tarot é um sistema de leitura de cartas que utiliza imagens e símbolos para fornecer insights e orientações sobre questões pessoais, profissionais e espirituais.\n\nJá a leitura de horóscopos é uma forma de adivinhação que utiliza a posição dos astros no momento do nascimento de uma pessoa para prever aspectos da sua personalidade e eventos da sua vida.")

def process_tarot_question(message, bot):
    """
    Processa a pergunta do usuário para leitura de Tarot
    """
    user_question = message.text
    drawn_cards = generate_cards()
    cards_message = "\n".join([f"{i+1}. {card}" for i, card in enumerate(drawn_cards)])
    response = (
        f"🧙‍♀️ Acabei de tirar do baralho algumas cartas aleatórias para você. Elas são:\n\n"
        f"{cards_message}\n\n"
    )
    bot.send_message(message.chat.id, response)
    sent_message = bot.send_message(message.chat.id, "🔮 Estou fazendo a leitura. Me dê uns segundinhos...")
    message_id = sent_message.message_id
    response = generate_response(user_question, cards_message)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message_id, text=response)
    bot.send_message(message.chat.id, "Espero que tenha gostado da consulta! 😉\n\nSelecione o que você deseja fazer agora:", reply_markup=get_main_keyboard())

def process_horoscope_question(message, bot):
    """
    Processa a pergunta do usuário para leitura de horóscopo
    """
    user_sign = message.text
    if user_sign in ZODIAC_SIGNS:
        sent_message = bot.send_message(message.chat.id, "🔮 Estou consultando as estrelas. Me dê uns segundinhos...")
        message_id = sent_message.message_id
        response = generate_response_horoscope(user_sign)

        if not response:
            bot.send_message(message.chat.id, "Desculpe, não consegui gerar seu horóscopo. Tente novamente mais tarde.")
            return

        bot.edit_message_text(chat_id=message.chat.id, message_id=message_id, text=response)
        bot.send_message(message.chat.id, "Espero que tenha gostado da consulta! 😉\n\nSelecione o que você deseja fazer agora:", reply_markup=get_main_keyboard())
    else:
        bot.send_message(message.chat.id, "Por favor, escolha um signo do zodíaco válido.", reply_markup=get_zodiac_keyboard()) 