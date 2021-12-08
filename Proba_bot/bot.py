import logging
from telegram.ext import Updater, CommandHandler
logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s', 
					level=logging.INFO, 
					filename='bot.log'
					)

#остановился на пятом шаге



def start_bot(update, bot):
	
	mytext = """Привет {}, 
я ничего не умею, 
кроме {}""".format(update.message.chat.username, '/start')

	update.message.reply_text(mytext)


def main():
	updtr = Updater('5000327713:AAF6-0Oj0ubvLyCSZj1R7Pm2Bo-SNJHIsss')
	updtr.dispatcher.add_handler(CommandHandler("start", start_bot))

	updtr.start_polling()
	updtr.idle()


if __name__ == "__main__":
	logging.info('bot_started')
	main()
