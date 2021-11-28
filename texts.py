import pyodbc
 
begin = "start"
begin_text="Welcome to my Bot"
customer = "Chef"
order_status = "waiting"

# first_food = 0
first_food_name="Plov"
price_1=10000
first_food_price=f"this food costs :   {price_1}  sum 😄\nname of food:   Plov"

# second_food = 0
second_food_name="Shashlik"
price_2=15000
second_food_price=f"this food costs :   {price_2} sum 🍞\nname of food:   Shashlik "

# third_food = 0
third_food_name="Shurpa"
price_3=20000
third_food_price=f"this food costs :    {price_3} 🥪 sum\nname of food:   Shurpa"

contact_button="Share_Contact"
contact_button_text="Please press to Button"

Basket="Basket"
Basket_adding="add to buskets🥡"


Menu="Menu"
Menu_text="choose what food you want😊😊😊"

Order_Status="order status"
Finish_Order="finish order! :("
Finish="Finished"

start_text="hello my dear , thanks for using this bot"



connection = pyodbc.connect(
    
    r"Driver={SQL Server};"
    "Server=sqltestbug.database.windows.net;"
    "Database=testdb;"
    "UID=testdb;"
    "PWD=Dotaru83")