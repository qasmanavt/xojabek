from requests.models import requote_uri
from telegram import *
from telegram.ext import *

phone_number2=""


def getContact(update: Update, context: CallbackContext):
    global phone_number1
    global phone_number2
    phone_number1 = update.message.contact.phone_number
    print(phone_number1)
    phone_number2=phone_number1
    print(phone_number2)

