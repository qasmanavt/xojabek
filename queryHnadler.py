from telegram import *
from telegram.ext import *
from requests import *
from pictures import *
from datetime import datetime 
from contac import *
from texts import *
from handler import *
def queryHandler(update: Update, context: CallbackContext):
    query = update.callback_query.data
    update.callback_query.answer()
    global first_food, second_food, third_food, order_status

    if "1" in query:
        context.bot.sendMediaGroup(chat_id=update.effective_chat.id, media=[InputMediaPhoto(
            get(first_food_url).content, caption="")])

        buttons = [[InlineKeyboardButton("add to buskets🥡", callback_data="first")],
                    [InlineKeyboardButton("finish order! :(", callback_data="tugadi")]]
        context.bot.send_message(chat_id=update.effective_chat.id,
                                    reply_markup=InlineKeyboardMarkup(buttons), text=first_food_price)
        

    elif "2" in query:

        context.bot.sendMediaGroup(chat_id=update.effective_chat.id, media=[InputMediaPhoto(
            get(second_food_url).content, caption="")])

        buttons = [[InlineKeyboardButton("add to buskets🥡", callback_data="second")],
                    [InlineKeyboardButton("finish order! :(", callback_data="tugadi")]]
        a = context.bot.send_message(chat_id=update.effective_chat.id,
                                        reply_markup=InlineKeyboardMarkup(buttons), text=second_food_price)
    

    elif "3" in query:
        context.bot.sendMediaGroup(chat_id=update.effective_chat.id, media=[InputMediaPhoto(
            get(third_food_url).content, caption="")])

        buttons = [[InlineKeyboardButton("add to buskets🥡", callback_data="third")],
                    [InlineKeyboardButton("finish order! :(", callback_data="tugadi")]]
        context.bot.send_message(chat_id=update.effective_chat.id,
                                    reply_markup=InlineKeyboardMarkup(buttons), text=third_food_price)

    elif "tugadi" in query:
        phone_number=phone_number2[0]
        
        context.bot.send_message(
            chat_id=update.effective_chat.id, text="finished")
        now = datetime.now()
        print(phone_number)
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

        buttons = [[InlineKeyboardButton(first_food_name, callback_data="1")],
                [InlineKeyboardButton(second_food_name, callback_data="2")],
                [InlineKeyboardButton(third_food_name, callback_data="3")]]
        context.bot.send_message(chat_id=update.effective_chat.id,
                                reply_markup=InlineKeyboardMarkup(buttons), text="choose what food you want😊😊😊")
                



    elif "first" in query:
        first_food += 1

        context.bot.send_message(chat_id=update.effective_chat.id,
                                    text=f"added {first_food}   to buskets 😄,if you want click again")
        
         

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