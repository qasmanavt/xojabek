import telegram
from config import TOKEN
from telegram import *
from telegram.ext import *
from requests import *
from pictures import *
from datetime import datetime, time
import time
from contac import *
from texts import *
from handler import *
from queryHnadler import *
from start import *
 
updater = Updater(TOKEN)
dispatcher = updater.dispatcher
bot = telegram.Bot(TOKEN)


 


dispatcher.add_handler(CallbackQueryHandler(queryHandler))
dispatcher.add_handler(CommandHandler("start", startCommand))
dispatcher.add_handler(MessageHandler(Filters.contact, getContact ))
dispatcher.add_handler(MessageHandler(Filters.text, messageHandler))


updater.start_polling()
