import telebot, time
from telebot import types
bot = telebot.TeleBot(token)

@bot.message_handler(commands = ["start"])
def start(message):
	keyboard_choice_language = types.InlineKeyboardMarkup()
	callback_button_language_english = types.InlineKeyboardButton(text = "English", callback_data = "english")
	callback_button_language_russian = types.InlineKeyboardButton(text = "Русский", callback_data = "russian")
	callback_button_language_spanish = types.InlineKeyboardButton(text = "Espanol", callback_data = "spanish")
	callback_button_language_turkish = types.InlineKeyboardButton(text = "Türkçe", callback_data = "turkish")
	keyboard_choice_language.add(callback_button_language_english, callback_button_language_russian)
	keyboard_choice_language.add(callback_button_language_spanish, callback_button_language_turkish)
	bot.send_message(message.from_user.id, "Hello! To begin with, its worth choosing the language we will speak.", reply_markup = keyboard_choice_language)

@bot.callback_query_handler(func = lambda call: True)
def language(call):
	if call.message:
		if call.data == "english":
			bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id, text = "Hello! I am a bot that will help you keep statistics in the chat. Just add me.")
		elif call.data == "russian":
			bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id, text = "Привет! Я бот, который поможет тебе вести статистику в чате. Просто добавь меня.")
		elif call.data == "spanish":
			bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id, text = "Hola! Soy un bot que te ayudará a mantener estadísticas en el chat. Solo agregame.")
		elif call.data == "turkish":
			bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id, text = "Selamlar! İstatistikleri sohbette tutmanıza yardımcı olacak bir botum. Sadece beni ekle.")

while True:
	try:
		bot.polling(none_stop = True)
	except Exception as e:
		time.sleep(2)
