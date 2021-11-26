from telegram import *
from telegram.ext import *
from requests import *
from pictures import *
from texts import *
import queryHnadler
import contac

def messageHandler(update: Update, context: CallbackContext):
      
    if begin in update.message.text:
        
    
        global phone_number
          
        
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
        order = ""
        price=0
        if queryHnadler.first_food>0:
            order = order +" "+ first_food_name+" :"+str(queryHnadler.first_food)+"\n"
            price=price+queryHnadler.first_food * price_1
        if queryHnadler.second_food>0:
            order = order +" "+ second_food_name+" :"+str(queryHnadler.second_food)+"\n"
            price = price + queryHnadler.second_food * price_2
        if queryHnadler.third_food>0:
            order = order + " "+third_food_name+" :"+str(queryHnadler.third_food)+"\n"
            price = price + queryHnadler.third_food * price_3
        
        text=order+"\n"+"Total price :"+str(price)+" sum"
         
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

        contac.phone_number2=cursor.fetchone()[0]
        connection.commit()

    

    if Order_Status in update.message.text:
        cursor = connection.cursor()
        cursor.execute(f'select top 1 status  from bot2 where phone_number=? order by time desc ;',contac.phone_number2)
        context.bot.send_message(chat_id=update.effective_chat.id,text=cursor.fetchone()[0])
        connection.commit()
    


