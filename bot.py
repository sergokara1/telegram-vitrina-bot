import telebot

TOKEN = "8485032335:AAFOaY8QRs3eB2h8c0YU6WzUUqMBJZYnKtM"
bot = telebot.TeleBot(TOKEN)

# Команда /start
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Привет! Это бот-витрина. Выберите команду:\n/catalog – каталог\n/help – помощь")

# Команда /catalog
@bot.message_handler(commands=['catalog'])
def catalog(message):
    bot.send_message(message.chat.id, "Каталог:\n1️⃣ Товар 1 – 100₽\n2️⃣ Товар 2 – 200₽\n3️⃣ Товар 3 – 300₽")

# Команда /help
@bot.message_handler(commands=['help'])
def help_cmd(message):
    bot.send_message(message.chat.id, "Команды:\n/start – начать\n/catalog – посмотреть товары\n/help – помощь")

# Ответ на любое другое сообщение
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.send_message(message.chat.id, "Я пока понимаю только команды /start, /catalog и /help.")

bot.polling(none_stop=True)
