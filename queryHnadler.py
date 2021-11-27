from requests import *
from pictures import *
from datetime import datetime 
from contac import *
from texts import *
import contac
def queryHandler(update: Update, context: CallbackContext):
    query = update.callback_query.data
    update.callback_query.answer()
    global first_food, second_food, third_food, order_status

    if "1" in query:
        context.bot.sendMediaGroup(chat_id=update.effective_chat.id, media=[InputMediaPhoto(
            get(first_food_url).content, caption="")])

        buttons = [[InlineKeyboardButton(Basket_adding, callback_data=first_food_name)],
                    [InlineKeyboardButton(Finish_Order, callback_data=Finish)]]
        context.bot.send_message(chat_id=update.effective_chat.id,
                                    reply_markup=InlineKeyboardMarkup(buttons), text=first_food_price)
        

    elif "2" in query:

        context.bot.sendMediaGroup(chat_id=update.effective_chat.id, media=[InputMediaPhoto(
            get(second_food_url).content, caption="")])

        buttons = [[InlineKeyboardButton(Basket_adding, callback_data=second_food_name)],
                    [InlineKeyboardButton(Finish_Order, callback_data=Finish)]]
        a = context.bot.send_message(chat_id=update.effective_chat.id,
                                        reply_markup=InlineKeyboardMarkup(buttons), text=second_food_price)
    

    elif "3" in query:
        context.bot.sendMediaGroup(chat_id=update.effective_chat.id, media=[InputMediaPhoto(
            get(third_food_url).content, caption="")])

        buttons = [[InlineKeyboardButton(Basket_adding, callback_data=third_food_name)],
                    [InlineKeyboardButton(Finish_Order, callback_data=Finish)]]
        context.bot.send_message(chat_id=update.effective_chat.id,
                                    reply_markup=InlineKeyboardMarkup(buttons), text=third_food_price)

    elif Finish in query:
        
        print(contac.phone_number2)
        context.bot.send_message(
            chat_id=update.effective_chat.id, text=Finish)
        now = datetime.now()
        
        cursor = connection.cursor()
        cursor.execute('insert into bot2 values (?,?,?,?,?,?,?,?);',
                        (first_food, second_food, third_food, update.effective_chat.full_name, update.effective_chat.id, order_status, now,contac.phone_number2))
        connection.commit()
        contac.phone_number2=""
        first_food=0
        second_food=0
        third_food=0
                  



    elif first_food_name in query:
        first_food += 1

        context.bot.send_message(chat_id=update.effective_chat.id,
                                    text=f"added {first_food}   to buskets 😄,if you want click again")
        
         

    elif second_food_name in query:
        second_food += 1

        context.bot.send_message(chat_id=update.effective_chat.id,
                                    text=f"added {second_food} 🍞 to buskets ,if you want click again")

    elif third_food_name in query:
        third_food += 1

        context.bot.send_message(chat_id=update.effective_chat.id,
                                    text=f"added {third_food}  🥪 to buskets,if you want click again")

    print(
        f"first food is {first_food}, second food {second_food}, third food {third_food}")