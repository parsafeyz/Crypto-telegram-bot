import requests
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

url = "https://api.binance.com/api/v3/ticker/price?symbol={name}"
TOKEN = "YOUR TOKEN"
bot = telebot.TeleBot(TOKEN)
msg = ""
temp = "temp"
data = ""


@bot.message_handler(commands = ['start'])
def send_welcome(message):
    bot.reply_to(message, "send *price* to see cryptos")

@bot.message_handler(commands = ['start'])
def send_p():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(
    InlineKeyboardButton("BNB in usdt", callback_data="BNB"),
    InlineKeyboardButton("BTC in usdt", callback_data="BTC"),
    InlineKeyboardButton("ETH in usdt", callback_data="ETH"),
    InlineKeyboardButton("TRX in usdt", callback_data="TRX"),
    InlineKeyboardButton("TWT in usdt", callback_data="TWT"),
    InlineKeyboardButton("ADA in usdt", callback_data="ADA"),
    InlineKeyboardButton("XRP in usdt", callback_data="XRP"),
    InlineKeyboardButton("SOL in usdt", callback_data="SOL"),
    InlineKeyboardButton("custom", callback_data="c"),
    )
    return markup

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    global msg
    print("pass")
    if call.data == "BNB":
        msg = "BNBUSDT"
        print(1)
    elif call.data == "BTC":
        msg = "BTCUSDT"
        print(2)
    elif call.data == "ETH":
        msg = "ETHUSDT"
    elif call.data == "TRX":
        msg = "TRXUSDT"
    elif call.data == "TWT":
        msg = "TWTUSDT"
    elif call.data == "ADA":
        msg = "ADAUSDT"
    elif call.data == "XRP":
        msg = "XRPUSDT"
    elif call.data == "SOL":
        msg = "SOLUSDT"

    temp = msg

    if callback_query != "c":
        print(temp)
        global response
        response = requests.get(f"https://api.binance.com/api/v3/ticker/price?symbol={msg}")
        temp = ""
        print(response.status_code)
        sp(temp)


@bot.message_handler(func=lambda m: True)
def sp(message):
    global response
    try:
        if message.text.lower() == "price":
            print(message.text.lower())
            bot.send_message(message.chat.id, "select one of crypto", reply_markup=send_p())
            global msg_id
            msg_id = message.chat.id
            print(msg_id)
    except AttributeError:
        pass

    if response.status_code == 200:
        data = response.json()
        print(type(data))
        print(data)
        print(f"{data['symbol']} price is {float(data['price'])}")

        bot.send_message(msg_id, f"{data['symbol']} price is {float(data['price'])}", reply_to_message_id=None)
    elif message.text.lower() == "price":
        pass
    else:
         bot.reply_to(message, "something is wrong")

bot.infinity_polling()
