import pyodbc

begin = "Start"
begin_text = "Welcome to my Bot ๐ค"
customer = "Chef"
order_status = "waiting"

# first_food = 0
first_food_name = "Plov"
price_1 = 10000
first_food_price = f"this food costs :   {price_1}  sum ๐\nname of food:   Plov ๐"

# second_food = 0
second_food_name = "Shashlik"
price_2 = 15000
second_food_price = f"this food costs :   {price_2} sum ๐\nname of food:   Shashlik ๐ "

# third_food = 0
third_food_name = "Shurpa"
price_3 = 20000
third_food_price = f"this food costs :    {price_3} ๐ sum\nname of food:   Shurpa ๐ฅฃ"

contact_button = "Share Contact"
contact_button_text = "Assalomu Aleykum, Please share your contact โ for using this bot "


Basket = "Basket ๐งบ"
Basket_adding = "Add to buskets ๐งบ"
Clear = "Clear"
Cleared_Text = "Your basket have been cleared ๐งบ"


Menu = "Menu ๐"
Menu_text = "Lets start our order ๐, what do you want to eat?"

Order_Status = "Order Status ๐ฆ"
Finish_Order = "Finish ๐ "
Finish = "Finished. For the peyment please type /shipping "


start_text = "Thanks for using this Bot ๐ช"
Back = "Back ๐"
Back2 = "Text"
Back2_text = "You are in main page ๐"


connection = pyodbc.connect(

    r"Driver={SQL Server};"
    "Server=sqltestbug.database.windows.net;"
    "Database=testdb;"
    "UID=testdb;"
    "PWD=Dotaru83")
