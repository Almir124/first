import telebot
from telebot.types import Message
from token_ import TOKEN_
import time
import datetime
import pytz

bot = telebot.TeleBot(TOKEN_)
@bot.message_handler(['start'])
def start(msg: telebot.types.Message):
    bot.send_message(msg.chat.id, f"Привет {msg.from_user.first_name}! Этот бот пока что ничего не умеет ")
    #а я просто комментарий


@bot.message_handler(['info'])#fghj
def info(msg: Message):
    #инфа о разработчике
    bot.send_message(msg.chat.id, f'Инфоомация разработчика(ФИО): Саляхов Альмир Артурович. \nПочта: asalyahov2007@gmail.com. \nТелеграмм: @almirthebest')

@bot.message_handler(['time'])
def time_(msg: Message):
    '''команда, которая напишет точное время и дату'''
    current_time = datetime.datetime.now().strftime('%H:%M:%S')
    current_date = datetime.date.today().strftime('%d/%m/%Y')

    time_moscow = pytz.timezone('Europe/Moscow')
    current_time_mos = datetime.datetime.now(time_moscow).strftime('%H:%M:%S   %d/%m/%Y')
    bot.send_message(msg.chat.id, f'Текущее время: {current_time}\nТекущая дата: {current_date}. \nТекущее время и дата в Москве: {current_time_mos}')

@bot.message_handler(['menu'])
def menu(msg: Message):
    '''команда, которая выдаст всевозможные команды для бота'''
    bot.send_message(msg.chat.id, '''Все доступные команды для бота: 
/time, /info''')




bot.infinity_polling()