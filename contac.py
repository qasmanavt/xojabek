from telegram import *
from telegram.ext import *
from texts import *
from pyodbc import *
from requests import *
from datetime import *
from time import *

phone_number2 = ""


def getContact(update: Update, context: CallbackContext):

    global phone_number2
    phone_number2 = update.message.contact.phone_number
    print(phone_number2)
    print(update.effective_chat.id)
    cursor = connection.cursor()
    cursor.execute('insert into bot2 (time, phone_number,first_food,second_food,third_food,id,status,name) values (?,?,?,?,?,?,?,?);',
                   (datetime.now(), phone_number2, 0, 0, 0, update.effective_chat.id, "waiting", update.effective_chat.full_name))
    connection.commit()

    buttons = [[KeyboardButton(begin)]]
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text=begin_text, reply_markup=ReplyKeyboardMarkup(buttons, resize_keyboard=True))
