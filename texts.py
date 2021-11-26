import pyodbc
begin = "start"
begin_text="Welcome to my Bot"
customer = "Chef"
order_status = "waiting"

first_food = 0
first_food_name="Plov"
first_food_price="this food costs :   10000 sum 😄\nname of food:   Plov"

second_food = 0
second_food_name="Shashlik"
second_food_price="this food costs :   15000 sum 🍞\nname of food:   sweets "

third_food = 0
third_food_name="Xanim"
third_food_price="this food costs :    20000 🥪 sum\nname of food:   eggs"

contact_button="Share_Contact"
contact_button_text="Please press to Button"

Basket="Basket"
Basket_adding="add to buskets🥡"





Menu="Menu"
Menu_text="choose what food you want😊😊😊"

Order_Status="order status"
Finish_Order="finish order! :("

start_text="hello my dear , thanks for using this bot"



connection = pyodbc.connect(
    "Driver={SQL Server Native Client 11.0};"
    "Server=LAPTOP-DFK8LR20;"
    "Database=testdb;"
    "Trusted_Connection=yes;")