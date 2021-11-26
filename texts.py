import pyodbc
begin = "start"
begin_text="Welcome to my Bot"
customer = "Chef"
order_status = "waiting"
first_food = 0
first_food_name="Plov"
second_food = 0
second_food_name="Shashlik"
third_food = 0
third_food_name="Xanim"

contact_button="Share_Contact"
contact_button_text="Please press to Button"

Basket="Basket"
Menu="Menu"

Order_Status="order status"

start_text="hello my dear , thanks for using this bot"



connection = pyodbc.connect(
    "Driver={SQL Server Native Client 11.0};"
    "Server=LAPTOP-DFK8LR20;"
    "Database=testdb;"
    "Trusted_Connection=yes;")