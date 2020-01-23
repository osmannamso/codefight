import telebot
from time import sleep
from parse import parse

bot = telebot.TeleBot('1034970709:AAFFgOSq8xz6Jv7Tqf3UM0zRyH5d9tvm9sA')
keyboard1 = telebot.types.ReplyKeyboardMarkup()
keyboard1.row('Привет', 'Пока')


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start', reply_markup=keyboard1)


@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, 'Привет, мой создатель')
    elif '/fight' in message.text.lower():
        bot.send_message(message.chat.id, 'geeks, ehhh, you could do something else\n')
        sleep(1)
        bot.send_message(message.chat.id, 'want to know results?')
        try:
            words = message.text.split(' ')
            if len(words) > 0:
                url = words[1]
                results = parse(url)
                bot.send_message(message.chat.id, results)
        except Exception as e:
            bot.send_message(message.chat.id, f'i was broken {e}')
    elif message.text.lower() == 'я тебя люблю':
        bot.send_sticker(message.chat.id, 'CAADAgADZgkAAnlc4gmfCor5YbYYRAI')


@bot.message_handler(content_types=['sticker'])
def sticker_id(message):
    print(message)


bot.polling()
