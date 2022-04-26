from telebot.types import KeyboardButton, ReplyKeyboardMarkup
from config import templates


def get_markup_of_products(list_product):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = []
    for product in list_product:
        buttons.append(KeyboardButton(product["productName"]))
    markup.add(*buttons)
    markup.add(KeyboardButton(templates["text_commands"]["back_menu"]))

    return markup


def get_markup_of_start():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(KeyboardButton(templates["text_commands"]["lactose_free"]),
               KeyboardButton(templates["text_commands"]["gluten_free"]))

    return markup
