from telegram.ext import *
from telegram import *
import message_handler

def start_with_shipping_callback(update: Update, context: CallbackContext):
    """Sends an invoice with shipping-payment."""
    chat_id = update.effective_chat.id
    title = "Payment"
    description = "Payment for ordering food"
    # select a payload just for you to recognize its the donation from your bot
    payload = "Custom-Payload"
    # In order to get a provider_token see https://core.telegram.org/bots/payments#getting-a-token
    provider_token = "398062629:TEST:999999999_F91D8F69C042267444B74CC0B3C747757EB0E065"
    currency = "UZS"
    # price in dollars
    print(message_handler.price_sum)
    price = message_handler.price_sum
    # price * 100 so as to include 2 decimal points
    # check https://core.telegram.org/bots/payments#supported-currencies for more details
    prices = [LabeledPrice("Test", price * 100)]

    # optionally pass need_name=True, need_phone_number=True,
    # need_email=True, need_shipping_address=True, is_flexible=True
    context.bot.send_invoice(
        chat_id,
        title,
        description,
        payload,
        provider_token,
        currency,
        prices,
        need_name=True,
        need_phone_number=True,
        # need_email=True,
        need_shipping_address=True,
        # is_flexible=True,
    )




