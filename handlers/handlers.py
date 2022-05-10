from config import bot, analyze, templates
from handlers.markup import get_markup_of_products, get_markup_of_start


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, templates["description"]["start"], reply_markup=get_markup_of_start())


@bot.message_handler(content_types='text')
def message_reply(message):

    if message.text == templates["text_commands"]["lactose_free"]:
        lactose_free = analyze.get_lactose_products()
        markup = get_markup_of_products(lactose_free)

        bot.send_message(message.chat.id, templates["description"]["type_product"], reply_markup=markup)

    elif message.text == templates["text_commands"]["gluten_free"]:
        lactose_free = analyze.get_gluten_products()
        markup = get_markup_of_products(lactose_free)

        bot.send_message(message.chat.id, templates["description"]["type_product"], reply_markup=markup)

    elif analyze.check_lactose_product(message.text):
        bot.send_message(message.chat.id, analyze.get_variations_text("lactoseFree", message.text))

    elif analyze.check_gluten_product(message.text):
        bot.send_message(message.chat.id, analyze.get_variations_text("glutenFree", message.text))

    elif message.text == templates["text_commands"]["back_menu"]:
        bot.send_message(message.chat.id, templates["description"]["back_menu"], reply_markup=get_markup_of_start())

    else:
        bot.send_message(message.chat.id, templates["description"]["try_again"])
