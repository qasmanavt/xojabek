from telegram import *
from telegram.ext import *
from requests import *
from pictures import *
from texts import *
from datetime import datetime
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
        global price_sum
        price_sum=0
      
        cursor = connection.cursor()
        b=cursor.execute('select top 1 first_food,second_food,third_food from bot2 where id=? order by time desc',update.effective_chat.id).fetchone()
        connection.commit()
        
        if  b[0]  >0:
            order = order +" "+ first_food_name+" :"+str( b[0])+"\n"
            price_sum=price_sum+ int(b[0]) * price_1
        if  b[1]   >0:
            order = order +" "+ second_food_name+" :"+str( b[1])+"\n"
            price_sum = price_sum +  b[1] * price_2
        if  b[2]  >0:
            order = order + " "+third_food_name+" :"+str( b[2])+"\n"
            price_sum = price_sum +  b[2] * price_3
        else:
            print("eeee")
        
        text=order+"\n"+"Total price :"+str(price_sum)+" sum"
         
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
        cursor = connection.cursor()
        cursor.execute('insert into bot2 (time, phone_number,first_food,second_food,third_food,id,name) values (?,?,?,?,?,?,?);',
                        (datetime.now(),contac.phone_number2,0,0,0,update.effective_chat.id,update.effective_chat.full_name))
        connection.commit()

    

    if Order_Status in update.message.text:
        id=update.effective_chat.id
        cursor = connection.cursor()
        cursor.execute(f'select phone_number  from bot2 where id=?  ;',id
                        )

        contac.phone_number2=cursor.fetchone()[0]
        
        connection.commit()
        cursor = connection.cursor()
        cursor.execute(f'select top 1 status  from bot2 where phone_number=? order by time desc ;',contac.phone_number2)
        context.bot.send_message(chat_id=update.effective_chat.id,text=cursor.fetchone()[0])
        connection.commit()
    


