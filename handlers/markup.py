from telebot.types import KeyboardButton, ReplyKeyboardMarkup


def get_markup_of_products(list_product):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = []
    for product in list_product:
        buttons.append(KeyboardButton(product["productName"]))
    markup.add(*buttons)

    return markup


def get_markup_of_start():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(KeyboardButton("Безлактозные продукты"), KeyboardButton("Безглютеновые продукты"))

    return markup