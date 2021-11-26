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
 
updater = Updater(TOKEN)
dispatcher = updater.dispatcher
bot = telegram.Bot(TOKEN)


 
def startCommand(update: Update, context: CallbackContext):
   

        
        
        contact_keyboard=[[KeyboardButton(text=contact_button, request_contact=True)]]  
     
        context.bot.send_message(chat_id=update.effective_chat.id,
                            text=contact_button_text, reply_markup=ReplyKeyboardMarkup(contact_keyboard))
        
        time.sleep(10)
 
        buttons = [[KeyboardButton(begin)]]
        context.bot.send_message(chat_id=update.effective_chat.id,
                            text=begin_text, reply_markup=ReplyKeyboardMarkup(buttons))


dispatcher.add_handler(CallbackQueryHandler(queryHandler))
dispatcher.add_handler(CommandHandler("start", startCommand))
dispatcher.add_handler(MessageHandler(Filters.contact, getContact ))
dispatcher.add_handler(MessageHandler(Filters.text, messageHandler))


updater.start_polling()
