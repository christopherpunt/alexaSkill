from yahoo_fin import stock_info as si
from datetime import date, timedelta

# logger = logging.getLogger(__name__)
# logger.setLevel(logging.INFO)

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


# class LaunchRequestHandler(AbstractRequestHandler):
#     """Handler for Skill Launch."""
#     def can_handle(self, handler_input):
#         # type: (HandlerInput) -> bool

#         return ask_utils.is_request_type("LaunchRequest")(handler_input)
        
#     def handle(self, handler_input):


#         speak_output = stockPrice("WM") + stockPrice("AAPL")

#         return (
#             handler_input.response_builder
#                 .speak(speak_output)
#                 # .ask(speak_output)
#                 .response
#         )
