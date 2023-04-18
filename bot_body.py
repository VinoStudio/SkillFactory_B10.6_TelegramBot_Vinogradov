#https://t.me/CurrencyExchangerProBot - ссылка на бота

import telebot
from config import *
from bot_exeptions import *

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message: telebot.types.Message):
    text = "Добро пожаловать на бота-помошника конвертации ваших валют с актуальным курсом рынка!\n\n\
Введите одну из актуальных команд для начала работы с ботом:\n\n\
→ /list - список доступных команд \n→ /help - инструкция по работе бота \n→ /values - доступные валюты"
    bot.reply_to(message, text)

@bot.message_handler(commands=['list'])
def list(message: telebot.types.Message):
    text = "Список актуальных комманд:\n\n→ /start - приветствие \n→ /help - инструкция \n" \
           "→ /values - список валют \n→ /list - список основных команд"
    bot.reply_to(message, text)

@bot.message_handler(commands=['help'])
def help(message: telebot.types.Message):
    text = "Для перевода валюты используйте следующую команду:\n\n\
<имя валюты>\t <в какую валюту перевести> \n<количество переводимой валюты>\n\n\
Например: Доллар Рубль 1 \n\nСписок всех доступных валют: /values"
    bot.reply_to(message, text)

@bot.message_handler(commands=['values'])
def available_values(message: telebot.types.Message):
    text = 'Доступные валюты:'
    for value in values:
        text = '\n'.join((text, f'- {value.title()}'))
    bot.reply_to(message, text)

@bot.message_handler(content_types=['video', 'sticker', 'video_note', 'photo', ])
def exeptions(message: telebot.types.Message):
    text = "А что, не плохо."
    bot.reply_to(message, text)

@bot.message_handler(content_types=['audio', 'voice', ])
def exeptions2(message: telebot.types.Message):
    text = "Какой красивый голос."
    bot.reply_to(message, text)

@bot.message_handler(content_types=['text', ])
def convert(message: telebot.types.Message):
    try:
        user_message = message.text.lower().split()

        if len(user_message) != 3:
            raise APIException('Указано неверное количество параметров')

        forth, into, amount = user_message
        convert = CryptoConverter.convert(forth, into, amount)

    except APIException as e:
        bot.reply_to(message, f'Ошибка от пользователя.\n{e}')

    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать команду.\n{e}')
    else:
        text = f'Из {amount}x {forth} вы получите → ' \
               f'{convert * float(amount.replace("," , "."))} {into}'
        bot.send_message(message.chat.id, text)


bot.polling()
