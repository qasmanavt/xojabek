from requests import *
from telegram import chat, message, messageid
from pictures import *
from datetime import datetime
from contac import *
from texts import *
import contac


def queryHandler(update: Update, context: CallbackContext):
    query = update.callback_query.data
    update.callback_query.answer()
    global order_status

    if "1" in query:
        context.bot.sendMediaGroup(chat_id=update.effective_chat.id, media=[InputMediaPhoto(
            get(first_food_url).content, caption="")])

        buttons = [[InlineKeyboardButton(Basket_adding, callback_data=first_food_name)], [InlineKeyboardButton(Back, callback_data=Back)]
                   ]

        context.bot.send_message(chat_id=update.effective_chat.id,
                                 reply_markup=InlineKeyboardMarkup(buttons), text=first_food_price)

    elif "2" in query:

        context.bot.sendMediaGroup(chat_id=update.effective_chat.id, media=[InputMediaPhoto(
            get(second_food_url).content, caption="")])

        buttons = [[InlineKeyboardButton(Basket_adding, callback_data=second_food_name)], [InlineKeyboardButton(Back, callback_data=Back)]
                   ]
        a = context.bot.send_message(chat_id=update.effective_chat.id,
                                     reply_markup=InlineKeyboardMarkup(buttons), text=second_food_price)

    elif "3" in query:
        buttons = [[InlineKeyboardButton(Basket_adding, callback_data=third_food_name)],
                   [InlineKeyboardButton(Back, callback_data=Back)]]
        context.bot.sendMediaGroup(chat_id=update.effective_chat.id, media=[InputMediaPhoto(
            get(third_food_url).content, caption="")])

        context.bot.send_message(chat_id=update.effective_chat.id,
                                 reply_markup=InlineKeyboardMarkup(buttons), text=third_food_price)

    elif Finish_Order in query:

        print(contac.phone_number2)
        context.bot.send_message(
            chat_id=update.effective_chat.id, text=Finish)
        cursor = connection.cursor()

        cursor.execute('update src set status=?  from (select top 1 * from bot2 where id=? order by time desc) src',
                       ("waiting", update.effective_chat.id))
        connection.commit()

        contac.phone_number2 = ""
    elif Clear in query:

        print(contac.phone_number2)
        context.bot.send_message(
            chat_id=update.effective_chat.id, text=Cleared_Text)
        cursor = connection.cursor()

        cursor.execute('update src set first_food=?,second_food=?,third_food=?  from (select top 1 * from bot2 where id=? order by time desc) src',
                       (0, 0, 0, update.effective_chat.id))
        connection.commit()

    elif Back in query:

        buttons = [[InlineKeyboardButton(first_food_name, callback_data="1")],
                   [InlineKeyboardButton(second_food_name, callback_data="2")],
                   [InlineKeyboardButton(third_food_name, callback_data="3")],
                   [InlineKeyboardButton(Back, callback_data=Back2)]]
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 reply_markup=InlineKeyboardMarkup(buttons), text=Menu_text)

    elif Back2 in query:
        context.bot.send_message(
            chat_id=update.effective_chat.id, text=Back2_text)

    elif first_food_name in query:

        cursor = connection.cursor()

        cursor.execute(
            'update src set first_food=first_food+1  from (select top 1 * from bot2 where id=? order by time desc) src', update.effective_chat.id)
        connection.commit()
        cursor = connection.cursor()
        first_food = cursor.execute(
            'select top 1 first_food  from bot2 where id=? order by time desc', update.effective_chat.id).fetchone()[0]
        connection.commit()

        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text=f"added {first_food}   to buskets 😄,if you want click again")

    elif second_food_name in query:

        cursor = connection.cursor()

        cursor.execute(
            'update src set second_food=second_food+1  from (select top 1 * from bot2 where id=? order by time desc) src', update.effective_chat.id)
        connection.commit()
        cursor = connection.cursor()
        second_food = cursor.execute(
            'select top 1 second_food  from bot2 where id=? order by time desc', update.effective_chat.id).fetchone()[0]
        connection.commit()

        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text=f"added {second_food} 🍞 to buskets ,if you want click again")

    elif third_food_name in query:

        cursor = connection.cursor()

        cursor.execute(
            'update src set third_food=third_food+1  from (select top 1 * from bot2 where id=? order by time desc) src', update.effective_chat.id)
        connection.commit()
        cursor = connection.cursor()
        third_food = cursor.execute(
            'select top 1 third_food  from bot2 where id=? order by time desc', update.effective_chat.id).fetchone()[0]
        connection.commit()

        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text=f"added {third_food}  🥪 to buskets,if you want click again")
    cursor = connection.cursor()
    b = cursor.execute('select top 1 first_food,second_food,third_food from bot2 where id=? order by time desc',
                       update.effective_chat.id).fetchone()
    connection.commit()

    print(
        f"first food is {b[0]}, second food {b[1]}, third food {b[2]}")
