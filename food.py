import telegram
from config import TOKEN
from telegram import *
from telegram.ext import *
from requests import *
from pictures import *
from contac import *
from texts import *
from message_handler import *
from queryHnadler import *
from start import *

order=""
 

if first_food>0:
    order = order + "first food count "+str(first_food)
if second_food>0:
    order = order + "second food count "+str(second_food)
if first_food>0:
    order = order + "third food count "+str(third_food)
