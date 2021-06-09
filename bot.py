import telebot
import config

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def start_message(message):
	chatId = message.chat.id
	text = message.text.lower
	bot.send_message(chatId, "теперь тут терри прачетт")

@bot.message_handler(content_types=['text'])
def send_message(message):
	chatId = message.chat.id
	text = message.text.lower()
	print(text)
	if text == "лови терри прачетта":
		bot.send_message(chatId, "поймал!")
	elif text == "не люблю терри прачетта":
		bot.send_message(chatId, "лох")
	elif text == "терри прачетт":
		p = open('C:\\Users\\sofya\\OneDrive\\Desktop\\tp.jpg', 'rb')
		bot.send_photo(chatId, 'https://fanzon-portal.ru/upload/iblock/0d6/0d67d869276134d7d5ffb4d1b17d5a2e.jpg')
	elif text == "че":
		bot.send_message(chatId, "терри прачетт")

bot.polling()
