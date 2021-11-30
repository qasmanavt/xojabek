import telegram
from config import TOKEN
from telegram import *
from telegram.ext import *
from requests import *
from pictures import *
from contac import *
from shipping import start_with_shipping_callback
from texts import *
from message_handler import *
from queryHnadler import *
from start import *
 
 
updater = Updater(TOKEN)
dispatcher = updater.dispatcher
bot = telegram.Bot(TOKEN)

dispatcher.add_handler(CallbackQueryHandler(queryHandler))
dispatcher.add_handler(CommandHandler("start", startCommand))
dispatcher.add_handler(CommandHandler("shipping", start_with_shipping_callback))
dispatcher.add_handler(MessageHandler(Filters.contact, getContact ))
dispatcher.add_handler(MessageHandler(Filters.text, messageHandler))



updater.start_polling()
