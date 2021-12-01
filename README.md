# This is a bot for  mini kitchen :)
First main.py file calls all of other files that contains for part of bot.

So start.py starts our bot and it will send contact button.

Then contac.py file receives this contact number and it will automaticly add user's data to AZURE SQL Database.It will also send start button.

messageHandler.py file sends keyboard buttons which is menu,basket and order status. then if user click one of them this file detects it and run requiered code
for example if user click menu it will show all of food names in list, for basket it shows count of fooods and amount using AZURE SQL Database. Order status also using this database for getting status

queryhandler.py is commands for inlinekeyboard. for example adding to busket or finishing order or menu list in conclusion it will take all of inlinequery codes

config.py file is a token of the bot

texts.py file involves all of the texts . example: buttons names(inline also keyboard), food names prices all of text and AZURE SQL Database connection also

pictures.py you can find all of pictures that used in this bot

shipping.py is a payment method logic that can show us after order finish

procfile is a file that i used to deploy to heroku but i have  some issue about it



