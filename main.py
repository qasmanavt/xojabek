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
        
      
def messageHandler(update: Update, context: CallbackContext):
      
    if begin in update.message.text:
        
    
        global first_food,second_food,third_food,phone_number
          
        
        button = [[KeyboardButton(Basket)], [KeyboardButton(Menu)], [
            KeyboardButton(Order_Status)]]

        context.bot.send_message(chat_id=update.effective_chat.id,
                                text=start_text, reply_markup=ReplyKeyboardMarkup(button))

        image = get(url).content
        context.bot.sendMediaGroup(chat_id=update.effective_chat.id, media=[
                                InputMediaPhoto(image, caption="")])

        buttons = [[InlineKeyboardButton(first_food_name, callback_data="1")],
                [InlineKeyboardButton(second_food_name, callback_data="2")],
                [InlineKeyboardButton(third_food_name, callback_data="3")]]
        context.bot.send_message(chat_id=update.effective_chat.id,
                                reply_markup=InlineKeyboardMarkup(buttons), text=Menu_text)

    if Basket in update.message.text:
        text = ("first food count "+str(first_food), "second food count "+str(second_food), "third food count "+str(third_food),
                "username "+str(update.effective_chat.full_name))
        context.bot.send_message(chat_id=update.effective_chat.id, text=text)
        

    if Menu in update.message.text:
        id=update.effective_chat.id
      


        image = get(url).content
        context.bot.sendMediaGroup(chat_id=update.effective_chat.id, media=[
                                   InputMediaPhoto(image, caption="")])

        buttons = [[InlineKeyboardButton(first_food_name, callback_data="1")],
                   [InlineKeyboardButton(second_food_name, callback_data="2")],
                   [InlineKeyboardButton(third_food_name, callback_data="3")]]
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 reply_markup=InlineKeyboardMarkup(buttons), text=Menu_text)
       
       
        cursor = connection.cursor()
        cursor.execute(f'select phone_number  from bot2 where id=?  ;',id
                        )

        phone_number=cursor.fetchone()[0]
        connection.commit()

    

    if Order_Status in update.message.text:
        cursor = connection.cursor()
        id = update.effective_chat.id
        cursor.execute(f'select top 1 status  from bot2 where phone_number=? order by time desc ;',phone_number2[0])
        context.bot.send_message(chat_id=update.effective_chat.id,text=cursor.fetchone()[0])
        connection.commit()
    

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


dispatcher.add_handler(CallbackQueryHandler(queryHandler))
dispatcher.add_handler(CommandHandler("start", startCommand))
dispatcher.add_handler(MessageHandler(Filters.contact, getContact ))
dispatcher.add_handler(MessageHandler(Filters.text, messageHandler))


updater.start_polling()
