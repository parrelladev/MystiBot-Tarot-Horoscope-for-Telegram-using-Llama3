import telebot
from config.settings import BOT_TOKEN
from core.handlers import (
    handle_start,
    handle_tarot,
    handle_horoscope,
    handle_info,
    handle_about
)
from utils.keyboards import get_main_keyboard

# Inicializando o bot com o token fornecido
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    handle_start(message, bot)

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    if message.text == "Realizar leitura de Tarot":
        handle_tarot(message, bot)
    elif message.text == "Entender o funcionamento do bot":
        handle_info(message, bot)
    elif message.text == "Aprender sobre Tarot e horóscopos":
        handle_about(message, bot)
    elif message.text == "Consultar meu horóscopo":
        handle_horoscope(message, bot)
    else:
        bot.send_message(message.chat.id, "🫠 Desculpe, não consegui entender sua escolha. Por favor, selecione uma das opções no menu:", reply_markup=get_main_keyboard())

def run_bot():
    """
    Inicia o bot
    """
    bot.polling() 