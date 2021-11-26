from telegram import *
from telegram.ext import *
from requests import *
from pictures import *
from datetime import   time
import time
from contac import *
from texts import *
from message_handler import *
from queryHnadler import *

def startCommand(update: Update, context: CallbackContext):
       

        
        
        contact_keyboard=[[KeyboardButton(text=contact_button, request_contact=True)]]  
     
        context.bot.send_message(chat_id=update.effective_chat.id,
                            text=contact_button_text, reply_markup=ReplyKeyboardMarkup(contact_keyboard))
        
        time.sleep(10)
 
        buttons = [[KeyboardButton(begin)]]
        context.bot.send_message(chat_id=update.effective_chat.id,
                            text=begin_text, reply_markup=ReplyKeyboardMarkup(buttons))
