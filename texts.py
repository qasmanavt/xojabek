import pyodbc

begin = "Start"
begin_text = "Welcome to my Bot 🤖"
customer = "Chef"
order_status = "waiting"

# first_food = 0
first_food_name = "Plov"
price_1 = 10000
first_food_price = f"this food costs :   {price_1}  sum 😄\nname of food:   Plov 🍚"

# second_food = 0
second_food_name = "Shashlik"
price_2 = 15000
second_food_price = f"this food costs :   {price_2} sum 😄\nname of food:   Shashlik 🍖 "

# third_food = 0
third_food_name = "Shurpa"
price_3 = 20000
third_food_price = f"this food costs :    {price_3} 😄 sum\nname of food:   Shurpa 🥣"

contact_button = "Share Contact"
contact_button_text = "Assalomu Aleykum, Please share your contact ☎ for using this bot "


Basket = "Basket 🧺"
Basket_adding = "Add to buskets 🧺"
Clear = "Clear"
Cleared_Text = "Your basket have been cleared 🧺"


Menu = "Menu 📋"
Menu_text = "Lets start our order 😊, what do you want to eat?"

Order_Status = "Order Status 📦"
Finish_Order = "Finish 🏁 "
Finish = "Finished. For the peyment please type /shipping "


start_text = "Thanks for using this Bot 💪"
Back = "Back 🔙"
Back2 = "Text"
Back2_text = "You are in main page 📄"


connection = pyodbc.connect(

    r"Driver={SQL Server};"
    "Server=sqltestbug.database.windows.net;"
    "Database=testdb;"
    "UID=testdb;"
    "PWD=Dotaru83")
