 
from telegram import *
from telegram.ext import *
from requests import *
from pictures import *
from contac import *
from texts import *
 

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
    
