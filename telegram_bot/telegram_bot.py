import telebot
import config

name = ''
surname = ''
age = 0

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    if message.text == "Привет":
        bot.reply_to(message, "Привет, человек!")
    elif message.text == "Hi":
        bot.reply_to(message, "Hi! My creator")
    elif message.text == '/reg':
        bot.send_message(message.from_user.id, "Привет! Давай познакомимся! Как тебя зовут?")
        bot.register_next_step_handler(message, reg_name)

    #bot.reply_to(message, message.text)

def reg_name(message):
    global name
    name = message.text
    bot.send_message(message.from_user.id, "Какая у тебя фамилия?")
    bot.register_next_step_handler(message, reg_surname)


def reg_surname(message):
    global surname
    surname = message.text
    bot.send_message(message.from_user.id, "Сколько тебе лет?")
    bot.register_next_step_handler(message, reg_age)


def reg_age(message):
    global age
    #age = message.text
    while age == 0:
        try:
            age = int(message.text)
        except Exceptiona:
            bot.send_message(message.from_user.id, "Вводите пожалуйста цифрами!")


bot.polling()