import telebot
import random

TOKEN = '7635241640:AAHodi2PDqvQV_fVMRsJ--yH6dkOGRfWZ-s'
bot = telebot.TeleBot(TOKEN)

# Список случайных фраз
phrases_byby = [
    "Пользователь {user} покинул нас. Прощай!",
    "Прощай, {user}!",
    "Не забывайте о нас, {user}!",
    "Надеюсь, {user} вернется к нам.",
    "Удачи, {user}!"
]

@bot.message_handler(commands=['start'])
def send_welcome(message):
    if message.chat.type == 'private':
        bot.reply_to(message, "Извините, я работаю только в группах.")

# Обработчик исключения пользователя
@bot.message_handler(content_types=['left_chat_member'])
def handle_left_member(message):
    user = message.left_chat_member.first_name
    phrase = random.choice(phrases_byby).format(user=user)
    bot.send_message(message.chat.id, phrase)

# Обработчик выхода пользователя
@bot.message_handler(content_types=['new_chat_members'])
def handle_new_member(message):
    for user in message.new_chat_members:
        if user.id == message.from_user.id:
            # Обработать выход пользователя
            phrase = random.choice(phrases_byby).format(user=user.first_name)
            bot.send_message(message.chat.id, phrase)

print("Бот успешно запущен!")

bot.polling()