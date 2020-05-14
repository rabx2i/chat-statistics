import telebot, time
from telebot import types
from database import check_db
from database import choice_language
bot = telebot.TeleBot(token)
check_db()

@bot.message_handler(commands = ["start"])
def start(message):
	keyboard_choice_language = types.ReplyKeyboardMarkup(True)
	button_language_english = types.InlineKeyboardButton(text = "English")
	button_language_russian = types.InlineKeyboardButton(text = "Russian")
	button_language_spanish = types.InlineKeyboardButton(text = "Spanish")
	button_language_turkish = types.InlineKeyboardButton(text = "Turkish")
	keyboard_choice_language.add(button_language_english, button_language_russian)
	keyboard_choice_language.add(button_language_spanish, button_language_turkish)
	bot.send_message(message.from_user.id, "Hello! To begin with, it’s worth choosing the language we will speak.", reply_markup = keyboard_choice_language)

@bot.message_handler(content_types = ["text"])
def dialogue(message):
	user_id = (message.from_user.id)
	if message.text == "English":
		language = "EN"
		choice_language(user_id = user_id, language = language)
		bot.send_message(message.from_user.id, "Hello! I’m a bot that will help you see the statistics in the chat. Just add me in him.")
	if message.text == "Russian":
		language = "RU"
		choice_language(user_id = user_id, language = language)
		bot.send_message(message.from_user.id, "Привет! Я бот, который поможет тебе посмотреть статистику в чате. Просто добавь меня в него.")
	elif message.text == "Spanish":
		language = "ES"
		choice_language(user_id = user_id, language = language)
		bot.send_message(message.from_user.id, "¡Hola! Soy un bot que te ayudará a ver las estadísticas en el chat. Solo agrégame en él.")
	elif message.text == "Turkish":
		language = "TR"
		choice_language(user_id = user_id, language = language)
		bot.send_message(message.from_user.id, "Merhaba! Ben sohbette istatistikleri görmenize yardımcı olacak bir botum. Sadece beni ekle.")

while True:
	try:
		bot.polling(none_stop = True)
	except Exception as e:
		time.sleep(2)