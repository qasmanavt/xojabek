import telegram
from config import TOKEN
from telegram import *
from telegram.ext import *
from requests import *
from pictures import *
from datetime import datetime

import pyodbc
 



phone_number=""
updater = Updater(TOKEN)
dispatcher = updater.dispatcher
bot = telegram.Bot(TOKEN)
user = "register"
customer = "Chef"
order_status = "waiting"
first_food = 0
second_food = 0
third_food = 0
connection = pyodbc.connect(
    "Driver={SQL Server Native Client 11.0};"
    "Server=LAPTOP-DFK8LR20;"
    "Database=testdb;"
    "Trusted_Connection=yes;"

)
def startCommand(update: Update, context: CallbackContext):
    buttons = [[KeyboardButton(user)]]
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text=" welcome to my bot!", reply_markup=ReplyKeyboardMarkup(buttons))

 
 

def messageHandler(update: Update, context: CallbackContext):
    
    if "register" in update.message.text:
        context.bot.send_message(chat_id=update.effective_chat.id,text="please write your phone number")
        print(update.message.text)
    if "99" in update.message.text:
        global phone_number,first_food,second_food,third_food
        phone_number=str(update.message.text)
        
        
        button = [[KeyboardButton("buskets")], [KeyboardButton("menu")], [
            KeyboardButton("order status")]]

        context.bot.send_message(chat_id=update.effective_chat.id,
                                text="hello my dear , thanks for using this bot", reply_markup=ReplyKeyboardMarkup(button))

        image = get(url).content
        context.bot.sendMediaGroup(chat_id=update.effective_chat.id, media=[
                                InputMediaPhoto(image, caption="")])

        buttons = [[InlineKeyboardButton("1", callback_data="1")],
                [InlineKeyboardButton("2", callback_data="2")],
                [InlineKeyboardButton("3", callback_data="3")]]
        context.bot.send_message(chat_id=update.effective_chat.id,
                                reply_markup=InlineKeyboardMarkup(buttons), text="choose what food you want😊😊😊")

    if "buskets" in update.message.text:
        text = ("first food count "+str(first_food), "second food count "+str(second_food), "third food count "+str(third_food),
                "username "+str(update.effective_chat.full_name))
        context.bot.send_message(chat_id=update.effective_chat.id, text=text)
        

    if "menu" in update.message.text:
        id=update.effective_chat.id
      


        image = get(url).content
        context.bot.sendMediaGroup(chat_id=update.effective_chat.id, media=[
                                   InputMediaPhoto(image, caption="")])

        buttons = [[InlineKeyboardButton("1", callback_data="1st")],
                   [InlineKeyboardButton("2", callback_data="2nd")],
                   [InlineKeyboardButton("3", callback_data="3rd")]]
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 reply_markup=InlineKeyboardMarkup(buttons), text="choose what food you want😊😊😊")
       
       
        cursor = connection.cursor()
        cursor.execute(f'select phone_number  from bot2 where id=?  ;',id
                        )

        phone_number=cursor.fetchone()[0]
        connection.commit()

    

    if "order status" in update.message.text:
        print("create")
        cursor = connection.cursor()

        id = update.effective_chat.id
        cursor.execute(f'select top 1 status  from bot2 where phone_number=? order by time desc ;',phone_number
                        )

        context.bot.send_message(chat_id=update.effective_chat.id,text=cursor.fetchone()[0])
        connection.commit()

    def queryHandler(update: Update, context: CallbackContext):
        query = update.callback_query.data
        update.callback_query.answer()
        global first_food, second_food, third_food, order_status,phone_number

        if "1" in query:
            context.bot.sendMediaGroup(chat_id=update.effective_chat.id, media=[InputMediaPhoto(
                get(first_food_url).content, caption="")])

            buttons = [[InlineKeyboardButton("add to buskets🥡", callback_data="first")],
                       [InlineKeyboardButton("finish order! :(", callback_data="tugadi")]]
            context.bot.send_message(chat_id=update.effective_chat.id,
                                     reply_markup=InlineKeyboardMarkup(buttons), text="this food costs :   10000 sum 😄\nname of food:   pizza")
           

        elif "2" in query:

            context.bot.sendMediaGroup(chat_id=update.effective_chat.id, media=[InputMediaPhoto(
                get(second_food_url).content, caption="")])

            buttons = [[InlineKeyboardButton("add to buskets🥡", callback_data="second")],
                       [InlineKeyboardButton("finish order! :(", callback_data="tugadi")]]
            a = context.bot.send_message(chat_id=update.effective_chat.id,
                                         reply_markup=InlineKeyboardMarkup(buttons), text="this food costs :   15000 sum 🍞\nname of food:   sweets ")
        

        elif "3" in query:
            context.bot.sendMediaGroup(chat_id=update.effective_chat.id, media=[InputMediaPhoto(
                get(third_food_url).content, caption="")])

            buttons = [[InlineKeyboardButton("add to buskets🥡", callback_data="third")],
                       [InlineKeyboardButton("finish order! :(", callback_data="tugadi")]]
            context.bot.send_message(chat_id=update.effective_chat.id,
                                     reply_markup=InlineKeyboardMarkup(buttons), text="this food costs :    20000 🥪 sum\nname of food:   eggs")

        elif "tugadi" in query:

            context.bot.send_message(
                chat_id=update.effective_chat.id, text="finished")
            now = datetime.now()

            cursor = connection.cursor()
            cursor.execute('insert into bot2 values (?,?,?,?,?,?,?,?);',
                           (first_food, second_food, third_food, update.effective_chat.full_name, update.effective_chat.id, order_status, now,phone_number))
            connection.commit()
            first_food=0
            second_food=0
            third_food=0
            image = get(url).content
            context.bot.sendMediaGroup(chat_id=update.effective_chat.id, media=[
                                    InputMediaPhoto(image, caption="")])

            buttons = [[InlineKeyboardButton("1", callback_data="1st")],
                    [InlineKeyboardButton("2", callback_data="2nd")],
                    [InlineKeyboardButton("3", callback_data="3rd")]]
            context.bot.send_message(chat_id=update.effective_chat.id,
                                    reply_markup=InlineKeyboardMarkup(buttons), text="choose what food you want😊😊😊")
                    



        elif "first" in query:
            first_food += 1

            a=context.bot.send_message(chat_id=update.effective_chat.id,
                                     text=f"added {first_food}   to buskets 😄,if you want click again")
            
            context.bot.editMessageText(update.effective_message.chat_id,text="added2")

        elif "second" in query:
            second_food += 1

            context.bot.send_message(chat_id=update.effective_chat.id,
                                     text=f"added {second_food} 🍞 to buskets ,if you want click again")

        elif "third" in query:
            third_food += 1

            context.bot.send_message(chat_id=update.effective_chat.id,
                                     text=f"added {third_food}  🥪 to buskets,if you want click again")

        print(
            f"first food is {first_food}, second food {second_food}, third food {third_food}")
    dispatcher.add_handler(CallbackQueryHandler(queryHandler))

 


dispatcher.add_handler(CommandHandler("start", startCommand))
dispatcher.add_handler(MessageHandler(Filters.text, messageHandler))

updater.start_polling()
