import requests
from bs4 import BeautifulSoup as b
import telebot
from telebot import types

URL_daily = 'https://74.ru/horoscope/daily/'
URL_tomorrow = 'https://74.ru/horoscope/tomorrow/'
API = '5348989589:AAHaCJyVCKlFIhOXAN2yJKvEv3uTHnA2GCI'


def parser_daily(url_daily):
    request_daily = requests.get(url_daily)
    soup = b(request_daily.text, 'html.parser')
    zodiac_daily = soup.find_all('div', class_='_2j-zP _1ylC5')
    return [clear.text for clear in zodiac_daily]


horoscope_daily = parser_daily(URL_daily)


def parser_tomorrow(url_tomorrow):
    request_tomorrow = requests.get(url_tomorrow)
    soup = b(request_tomorrow.text, 'html.parser')
    zodiac_tomorrow = soup.find_all('div', class_='_2j-zP _1ylC5')
    return [clear.text for clear in zodiac_tomorrow]


horoscope_tomorrow = parser_tomorrow(URL_tomorrow)

bot = telebot.TeleBot(API)


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button = types.KeyboardButton('Узнать гороскоп')
    markup.add(button)
    bot.send_message(message.chat.id, text='Привет!'.format(message.from_user), reply_markup=markup)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == 'Узнать гороскоп':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        today_button = types.KeyboardButton('Сегодня')
        tomorrow_button = types.KeyboardButton('Завтра')
        back_button = types.KeyboardButton('Вернуться в главное меню')
        keyboard.add(today_button, tomorrow_button, back_button)
        bot.send_message(message.chat.id, text='На какой день Вы хотите узнать гороскоп?', reply_markup=keyboard)
    elif message.text == 'Вернуться в главное меню':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        learn_button = types.KeyboardButton('Узнать гороскоп')
        keyboard.add(learn_button)
        bot.send_message(message.chat.id, text='Вы вернулись в главное меню', reply_markup=keyboard)
    elif message.text == 'Сегодня':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        learn_button = types.KeyboardButton('Узнать гороскоп')
        keyboard.add(learn_button)
        bot.send_message(message.chat.id, text='Вы выбрали "Сегодня"', reply_markup=keyboard)
        keyboard_2 = types.InlineKeyboardMarkup(row_width=2)
        oven_button = types.InlineKeyboardButton(text='♈ Овен ♈', callback_data='oven')
        telec_button = types.InlineKeyboardButton(text='♉ Телец ♉', callback_data='telec')
        bliznecy_button = types.InlineKeyboardButton(text='♊ Близнецы ♊', callback_data='bliznecy')
        rak_button = types.InlineKeyboardButton(text='♋ Рак ♋', callback_data='rak')
        lev_button = types.InlineKeyboardButton(text='♌ Лев ♌', callback_data='lev')
        deva_button = types.InlineKeyboardButton(text='♍ Дева ♍', callback_data='deva')
        vesy_button = types.InlineKeyboardButton(text='♎ Весы ♎', callback_data='vesy')
        scorpion_button = types.InlineKeyboardButton(text='♏ Скорпион ♏', callback_data='scorpion')
        strelec_button = types.InlineKeyboardButton(text='♐ Стрелец ♐', callback_data='strelec')
        koserog_button = types.InlineKeyboardButton(text='♑ Козерог ♑', callback_data='koserog')
        vodoley_button = types.InlineKeyboardButton(text='♒ Водолей ♒', callback_data='vodoley')
        ryby_button = types.InlineKeyboardButton(text='♓ Рыбы ♓', callback_data='ryby')
        keyboard_2.add(oven_button, telec_button, bliznecy_button, rak_button, lev_button, deva_button, vesy_button,
                       scorpion_button, strelec_button, koserog_button, vodoley_button, ryby_button)
        bot.send_message(message.from_user.id, text='Выберите свой знак зодиака', reply_markup=keyboard_2)
    elif message.text == 'Завтра':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        learn_button = types.KeyboardButton('Узнать гороскоп')
        keyboard.add(learn_button)
        bot.send_message(message.chat.id, text='Вы выбрали "Завтра"', reply_markup=keyboard)
        keyboard_2 = types.InlineKeyboardMarkup(row_width=2)
        oven_button = types.InlineKeyboardButton(text='♈ Овен ♈', callback_data='oven_tomorrow')
        telec_button = types.InlineKeyboardButton(text='♉ Телец ♉', callback_data='telec_tomorrow')
        bliznecy_button = types.InlineKeyboardButton(text='♊ Близнецы ♊', callback_data='bliznecy_tomorrow')
        rak_button = types.InlineKeyboardButton(text='♋ Рак ♋', callback_data='rak_tomorrow')
        lev_button = types.InlineKeyboardButton(text='♌ Лев ♌', callback_data='lev_tomorrow')
        deva_button = types.InlineKeyboardButton(text='♍ Дева ♍', callback_data='deva_tomorrow')
        vesy_button = types.InlineKeyboardButton(text='♎ Весы ♎', callback_data='vesy_tomorrow')
        scorpion_button = types.InlineKeyboardButton(text='♏ Скорпион ♏', callback_data='scorpion_tomorrow')
        strelec_button = types.InlineKeyboardButton(text='♐ Стрелец ♐', callback_data='strelec_tomorrow')
        koserog_button = types.InlineKeyboardButton(text='♑ Козерог ♑', callback_data='koserog_tomorrow')
        vodoley_button = types.InlineKeyboardButton(text='♒ Водолей ♒', callback_data='vodoley_tomorrow')
        ryby_button = types.InlineKeyboardButton(text='♓ Рыбы ♓', callback_data='ryby_tomorrow')
        keyboard_2.add(oven_button, telec_button, bliznecy_button, rak_button, lev_button, deva_button, vesy_button,
                       scorpion_button, strelec_button, koserog_button, vodoley_button, ryby_button)
        bot.send_message(message.from_user.id, text='Выберите свой знак зодиака', reply_markup=keyboard_2)
    else:
        bot.send_message(message.chat.id, text='Я Вас не понимаю! Пользуйтесь меню.')


@bot.callback_query_handler(func=lambda call: True)
def callback_inline_daily(call):
    if call.data == 'oven':
        bot.send_message(call.message.chat.id, '♈ Овен ♈')
        bot.send_message(call.message.chat.id, horoscope_daily[0])
    elif call.data == 'telec':
        bot.send_message(call.message.chat.id, '♉ Телец ♉')
        bot.send_message(call.message.chat.id, horoscope_daily[1])
    elif call.data == 'bliznecy':
        bot.send_message(call.message.chat.id, '♊ Близнецы ♊')
        bot.send_message(call.message.chat.id, horoscope_daily[2])
    elif call.data == 'rak':
        bot.send_message(call.message.chat.id, '♋ Рак ♋')
        bot.send_message(call.message.chat.id, horoscope_daily[3])
    elif call.data == 'lev':
        bot.send_message(call.message.chat.id, '♌ Лев ♌')
        bot.send_message(call.message.chat.id, horoscope_daily[4])
    elif call.data == 'deva':
        bot.send_message(call.message.chat.id, '♍ Дева ♍')
        bot.send_message(call.message.chat.id, horoscope_daily[5])
    elif call.data == 'vesy':
        bot.send_message(call.message.chat.id, '♎ Весы ♎')
        bot.send_message(call.message.chat.id, horoscope_daily[6])
    elif call.data == 'scorpion':
        bot.send_message(call.message.chat.id, '♏ Скорпион ♏')
        bot.send_message(call.message.chat.id, horoscope_daily[7])
    elif call.data == 'strelec':
        bot.send_message(call.message.chat.id, '♐ Стрелец ♐')
        bot.send_message(call.message.chat.id, horoscope_daily[8])
    elif call.data == 'koserog':
        bot.send_message(call.message.chat.id, '♑ Козерог ♑')
        bot.send_message(call.message.chat.id, horoscope_daily[9])
    elif call.data == 'vodoley':
        bot.send_message(call.message.chat.id, '♒ Водолей ♒')
        bot.send_message(call.message.chat.id, horoscope_daily[10])
    elif call.data == 'ryby':
        bot.send_message(call.message.chat.id, '♓ Рыбы ♓')
        bot.send_message(call.message.chat.id, horoscope_daily[11])
    elif call.data == 'oven_tomorrow':
        bot.send_message(call.message.chat.id, '♈ Овен ♈')
        bot.send_message(call.message.chat.id, horoscope_tomorrow[0])
    elif call.data == 'telec_tomorrow':
        bot.send_message(call.message.chat.id, '♉ Телец ♉')
        bot.send_message(call.message.chat.id, horoscope_tomorrow[1])
    elif call.data == 'bliznecy_tomorrow':
        bot.send_message(call.message.chat.id, '♊ Близнецы ♊')
        bot.send_message(call.message.chat.id, horoscope_tomorrow[2])
    elif call.data == 'rak_tomorrow':
        bot.send_message(call.message.chat.id, '♋ Рак ♋')
        bot.send_message(call.message.chat.id, horoscope_tomorrow[3])
    elif call.data == 'lev_tomorrow':
        bot.send_message(call.message.chat.id, '♌ Лев ♌')
        bot.send_message(call.message.chat.id, horoscope_tomorrow[4])
    elif call.data == 'deva_tomorrow':
        bot.send_message(call.message.chat.id, '♍ Дева ♍')
        bot.send_message(call.message.chat.id, horoscope_tomorrow[5])
    elif call.data == 'vesy_tomorrow':
        bot.send_message(call.message.chat.id, '♎ Весы ♎')
        bot.send_message(call.message.chat.id, horoscope_tomorrow[6])
    elif call.data == 'scorpion_tomorrow':
        bot.send_message(call.message.chat.id, '♏ Скорпион ♏')
        bot.send_message(call.message.chat.id, horoscope_tomorrow[7])
    elif call.data == 'strelec_tomorrow':
        bot.send_message(call.message.chat.id, '♐ Стрелец ♐')
        bot.send_message(call.message.chat.id, horoscope_tomorrow[8])
    elif call.data == 'koserog_tomorrow':
        bot.send_message(call.message.chat.id, '♑ Козерог ♑')
        bot.send_message(call.message.chat.id, horoscope_tomorrow[9])
    elif call.data == 'vodoley_tomorrow':
        bot.send_message(call.message.chat.id, '♒ Водолей ♒')
        bot.send_message(call.message.chat.id, horoscope_tomorrow[10])
    elif call.data == 'ryby_tomorrow':
        bot.send_message(call.message.chat.id, '♓ Рыбы ♓')
        bot.send_message(call.message.chat.id, horoscope_tomorrow[11])
    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Ваш гороскоп',
                          reply_markup=None)


bot.polling(none_stop=True, interval=0)
