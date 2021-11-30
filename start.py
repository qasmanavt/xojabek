from telegram import *
from telegram.ext import *
from texts import *
 
 

def startCommand(update: Update, context: CallbackContext):
       

        
        
        contact_keyboard=[[KeyboardButton(text=contact_button, request_contact=True)]]  
     
        context.bot.send_message(chat_id=update.effective_chat.id,
                            text=contact_button_text, reply_markup=ReplyKeyboardMarkup(contact_keyboard))
        
   
