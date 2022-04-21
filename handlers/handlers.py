from telebot.types import KeyboardButton, ReplyKeyboardMarkup
from config import bot, analyze


@bot.message_handler(commands=['start'])
def start(message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(KeyboardButton("Безлактозные продукты"), KeyboardButton("Безглютеновые продукты"))

    bot.send_message(message.chat.id, "Привет! Я помогу составить тебе рацион питания. "
                                      "Выбери следующий шаг.", reply_markup=markup)


@bot.message_handler(content_types='text')
def message_reply(message):

    if message.text == "Безлактозные продукты":
        markup = ReplyKeyboardMarkup(resize_keyboard=True)
        lactose_free = analyze.get_lactose_products()

        for product in lactose_free:
            markup.add(KeyboardButton(product["productName"]))
        bot.send_message(message.chat.id, "Отлично, выберите одну из следующих категорий", reply_markup=markup)

    elif message.text == "Безглютеновые продукты":
        bot.send_message(message.chat.id, "Супер, выберите одну из следующих категорий")

    elif analyze.check_lactose_product(message.text):
        bot.send_message(message.chat.id, analyze.get_variations_text("lactoseFree", message.text))

    elif analyze.check_gluten_product(message.text):
        bot.send_message(message.chat.id, analyze.get_variations_text("glutenFree", message.text))

    else:
        bot.send_message(message.chat.id, "Попробуйте заново")
