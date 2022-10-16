import logging #dokumentiert was gemacht, eingegeben wurde 
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import settings

logging.basicConfig(filename='bot.log', level=logging.INFO)

def main():
    # variable als Updater definieren, Schlüssel vom Telegram Botfather
    mybot = Updater(settings.API_KEY, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    logging.info("bot started")
    # bot schickt server nachrichten und fragt nach neuem vom user
    mybot.start_polling()
    # bot macht immer weiter, schickt nachrichten, bis man prozess in comand line abbricht (WICHTIG!)
    mybot.idle()

def greet_user(update, context):
    print('pressed /start')
    update.message.reply_text('hello User, you have pressed /start')

# nimmt user text und wiederholt ihn (Echo)
def talk_to_me(update, context):
    user_text = update.message.text 
    print(user_text)
    update.message.reply_text(user_text)

if __name__ == "__main__":
    main() 
    