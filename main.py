import telebot
from telebot import types

bot = telebot.TeleBot('5749124923:AAG4-Q5f3ddfCduhRR94QJ8ie6QRaowVsDc')


@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Привет, <b>{message.from_user.first_name} нажми на /tits</b>'
    bot.send_message(message.chat.id, mess, parse_mode='html')


# @bot.message_handler(content_types=['text'])
# def get_user_text(message):
#     if message.text == 'Hello':
#         bot.send_message(message.chat.id, 'И тебе привет', parse_mode='html')
#     elif message.text == 'id':
#         bot.send_message(message.chat.id, f'Твой ID: {message.from_user.id}', parse_mode='html')
#     elif message.text == 'photo':
#         photo = open('cat.jpg', 'rb')
#         bot.send_photo(message.chat.id, photo)
#     else:
#         bot.send_message(message.chat.id, 'Я тебя не понимаю', parse_mode='html')


@bot.message_handler(content_types=['photo'])
def get_user_photo(message):
    bot.send_message(message.chat.id, 'Вау, крутое фото!')


@bot.message_handler(commands=['kitty'])
def photo(message):
    message.text = 'photo'
    photo = open('cat.jpg', 'rb')
    bot.send_photo(message.chat.id, photo)


@bot.message_handler(commands=['website'])
def website(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Посетить веб сайт', url='https://find-routee.herokuapp.com/'))
    bot.send_message(message.chat.id, 'Перейдите на сайт', reply_markup=markup)


@bot.message_handler(commands=['tits'])
def website(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    website = types.KeyboardButton('/website')
    start = types.KeyboardButton('/kitty')
    markup.add(website, start)
    bot.send_message(message.chat.id, 'Перейдите на сайт', reply_markup=markup)


bot.polling(none_stop=True)
