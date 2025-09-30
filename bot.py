import telebot
from transliterate import to_cyrillic, to_latin

TOKEN = "6225450028:AAFr5pfnBOtUibQmPXe6pp6diNvvUb1qMbM"
bot = telebot.TeleBot(token=TOKEN)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    """bot"""
    username = message.from_user.username
    xabar = f"Assalomu alaykum, {username}!\nKirill-Lotin-Kirill botiga xush kelibsiz!"
    xabar += "\nMatningizni yuboring."
    bot.reply_to(message, xabar)


@bot.message_handler(func=lambda msg: msg.text is not None)
def translit(message):
    """Oynaymiz"""
    msg = message.text
    if msg.isascii():
        javob = to_cyrillic(msg)
    else:
        javob = to_latin(msg)
    bot.reply_to(message, javob)


bot.polling(none_stop=True)
