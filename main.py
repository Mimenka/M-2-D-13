import telebot
from telebot import types

token = '7049960767:AAGcflss4z2VU3T4hbpmn_XcxO2rSjxekGc'
bot = telebot.TeleBot(token=token, parse_mode=None)



@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Welcome to Domino's pizza. Choose what you want?")
    markup = types.ReplyKeyboardMarkup(row_width=2)
    btn1 = types.KeyboardButton('Rim-Pizza')
    btn2 = types.KeyboardButton('Sandwhiches')
    btn3 = types.KeyboardButton('Ice cream')
    btn4 = types.KeyboardButton('Mod Pizza')
    markup.add(btn1,btn2,btn3,btn4)
    
    bot.send_message(message.chat.id, 'choose one options',reply_markup=markup)


@bot.message_handler(func=lambda x: True)
def echo_all(message):
    bot.reply_to(message,'Button was clicked')


bot.polling()