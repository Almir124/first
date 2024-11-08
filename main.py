import telebot
from telebot.types import Message
from token_ import TOKEN_

bot = telebot.TeleBot(TOKEN_)
@bot.message_handler(content_types=['text'])
def start(msg: telebot.types.Message):
    bot.send_message(msg.chat.id, f"Привет {msg.from_user.first_name}!")
  
bot.infinity_polling()
