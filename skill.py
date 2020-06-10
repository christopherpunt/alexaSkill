from yahoo_fin import stock_info as si
from datetime import date, timedelta

# print(si.get_live_price("WM"))

# today = date.today()
# yesterday = today - timedelta(days = 7)
# date = today.strftime("%m/%d/%Y")
# yesterdaydate = yesterday.strftime("%m/%d/%Y")
# print(date)
# print(yesterdaydate)

# data = si.get_data("WM").tail(1)
# print(type(data))
# print(data)
# print(data.iloc[-1]["open"])

def stockPrice(ticker):

    currentPrice = si.get_live_price(ticker)
    currentDollars = str(round(currentPrice, 2)).split(".")[0]
    currentCents = str(round(currentPrice, 2)).split(".")[1]

    speakCurrentPrice = ticker + " is at " + currentDollars + " dollars and " + currentCents + " cents"

    data = si.get_data(ticker).tail(2)

    prevClosedPrice = data.iloc[-2]["close"]

    changeToday = currentPrice - prevClosedPrice 

    if changeToday >= 0:
        downUp = "up"
    else:
        downUp = "down"

    changeToday = str(round(abs(changeToday), 2))

    dollars = changeToday.split(".")[0]
    cents = changeToday.split(".")[1]

    speakChangeToday = "Which is " + downUp + " " + dollars + " dollars and " + cents + " cents today"

    pause = "<break time= '1s'/>"
    return speakCurrentPrice + pause + speakChangeToday + pause






print(stockPrice("WM") + stockPrice("AAPL"))


# print(si.get_open("WM"))

# from yahoo_finance import Share

# wm = Share('WM')

# print(wm.get_open())
# print(wm.get_price())

# from yfinance as yf

# wm = yf.Ticker("WM")


# import datetime as dt
# import matplotlib.pyplot as plt
# from matplotlib import style
# import pandas as pd
# import pandas_datareader.data as web

# style.use('ggplot')

# start = dt.datetime(2015, 1, 1)
# end = dt.datetime.now()
# df = web.DataReader("WM", 'morningstar', start, end)
# df.reset_index(inplace=True)
# df.set_index("Date", inplace=True)
# df = df.drop("Symbol", axis=1)

# print(df.head())









from yahoo_fin import stock_info as si


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

def stockPrice(ticker):
    currentPrice = si.get_live_price(ticker)
    currentDollars = str(round(currentPrice, 2)).split(".")[0]
    currentCents = str(round(currentPrice, 2)).split(".")[1]

    speakCurrentPrice = ticker + " is at " + currentDollars + " dollars and " + currentCents + " cents "

    data = si.get_data(ticker).tail(2)

    prevClosedPrice = data.iloc[-2]["close"]

    changeToday = currentPrice - prevClosedPrice 

    if changeToday >= 0:
        downUp = "up"
    else:
        downUp = "down"

    changeToday = str(round(abs(changeToday), 2))

    dollars = changeToday.split(".")[0]
    cents = changeToday.split(".")[1]

    speakChangeToday = "Which is " + downUp + " " + dollars + " dollars and " + cents + " cents today"

    pause = "<break time= '1s'/>"
    return speakCurrentPrice + pause + speakChangeToday + pause


class LaunchRequestHandler(AbstractRequestHandler):
    """Handler for Skill Launch."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool

        return ask_utils.is_request_type("LaunchRequest")(handler_input)
        
    def handle(self, handler_input):


        speak_output = stockPrice("WM") + stockPrice("AAPL")

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask(speak_output)
                .response
        )
