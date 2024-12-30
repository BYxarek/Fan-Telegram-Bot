import telebot
import random

TOKEN = 'Telegram_bot_token'
bot = telebot.TeleBot(TOKEN)

# Список случайных фраз
phrases_hello = [
    "Добро пожаловать, {user}!",
    "Привет, {user}!",
    "Рады видеть тебя, {user}!",
    "Приветствуем, {user}!",
    "Добро пожаловать в наш чат, {user}!"
]

phrases_byby = [
    "Пользователь {user} покинул нас. Прощай!",
    "Прощай, {user}!",
    "Не забывайте о нас, {user}!",
    "Надеюсь, {user} вернется к нам.",
    "Удачи, {user}!"
]

phrases_thankful = [
    "Спасибо, что добавили меня в чат! Мой исходный код есть на GitHub (не забудь подписаться и поставить звезду) - https://github.com/BYxarek/Fan-Telegram-Bot"
]

@bot.message_handler(commands=['start', 'why'])
def send_welcome(message):
    if message.chat.type == 'private':
        bot.reply_to(message, "Извините, я работаю только в группах.")
    elif message.text == "/why":
        bot.reply_to(message, "Функции бота:\n"
                             "1. Приветствие новых пользователей.\n"
                             "2. Прощание с пользователями, покидающими чат.\n"
                             "3. Благодарность при добавлении бота в чат.")

# Обработчик исключения пользователя
@bot.message_handler(content_types=['left_chat_member'])
def handle_left_member(message):
    user = message.left_chat_member.first_name
    phrase = random.choice(phrases_byby).format(user=user)
    bot.send_message(message.chat.id, phrase)

# Обработчик нового пользователя
@bot.message_handler(content_types=['new_chat_members'])
def handle_new_member(message):
    for user in message.new_chat_members:
        if user.id == bot.get_me().id:
            # Отправить благодарственное сообщение
            phrase = random.choice(phrases_thankful)
            bot.send_message(message.chat.id, phrase)
        else:
            # Обработать приветствие пользователя
            phrase = random.choice(phrases_hello).format(user=user.first_name)
            bot.send_message(message.chat.id, phrase)

# Обработчик пользователя, который входит в чат по ссылке-приглашению
@bot.message_handler(content_types=['member_invited'])
def handle_invited_member(message):
    user = message.invited_chat_member.first_name
    phrase = random.choice(phrases_hello).format(user=user)
    bot.send_message(message.chat.id, phrase)

print("Бот успешно запущен!")

bot.polling(none_stop=True)