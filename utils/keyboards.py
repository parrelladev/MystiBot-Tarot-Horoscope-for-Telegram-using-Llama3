import telebot
from constants.tarot_cards import ZODIAC_SIGNS

def get_main_keyboard():
    markup = telebot.types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    item1 = telebot.types.KeyboardButton("Entender o funcionamento do bot")
    item2 = telebot.types.KeyboardButton("Aprender sobre Tarot e horóscopos")
    item3 = telebot.types.KeyboardButton("Realizar leitura de Tarot")
    item4 = telebot.types.KeyboardButton("Consultar meu horóscopo")
    markup.add(item1, item2, item3, item4)
    return markup

def get_zodiac_keyboard():
    zodiac_markup = telebot.types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    for sign in ZODIAC_SIGNS:
        zodiac_markup.add(telebot.types.KeyboardButton(sign))
    return zodiac_markup 