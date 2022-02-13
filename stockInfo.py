import yfinance as yf
from rpi_lcd import LCD
import time

lcd = LCD()
tickers = ["AAPL", "AMZN", "MSFT", "TSLA"]
ticker_comp_names = ["Apple", "Amazon", "Microsoft", "Tesla"]

def get_current_price(ticker):
    todays_data = ticker.history(period='1d')
    price=  todays_data['Close'][0]
    return price

def get_last_close(ticker):
    todays_data = ticker.history(period='5d')
    price=  todays_data['Close'][3]
    return price
def startup():
    lcd.clear()
    ticker = yf.Ticker(tickers[0])
    current_price = get_current_price(ticker)
    last_close = get_last_close(ticker)
    percent_change = ((current_price - last_close)/last_close)*100   
    line1 =  tickers[0] + '(' + ticker_comp_names[0] + ')'
    line2 = "price: " + "$" + format(current_price, ",.2f")
    if percent_change>0:
            line3 = "+" + format(percent_change, ",.2f") + "% up today"
    else:
        line3 = format(percent_change, ",.2f") + "% down today"

    lcd.clear()
    lcd.text(line1,1)
    lcd.text(line2,2)
    lcd.text(str(line3),4)
    time.sleep(3)

def show():
    startup()
    x = len(tickers)
    i =0
    run=True
    while run:
        ticker = yf.Ticker(tickers[i])
        current_price = get_current_price(ticker)
        last_close = get_last_close(ticker)
        percent_change = ((current_price - last_close)/last_close)*100   
        line1 =  tickers[i] + '(' + ticker_comp_names[i] + ')'
        line2 = "price: " + "$" + format(current_price, ",.2f")
        if percent_change>0:
            line3 = "+" + format(percent_change, ",.2f") + "% up today"
        else:
            line3 = format(percent_change, ",.2f") + "% down today"

        lcd.clear()
        lcd.text(line1,1)
        lcd.text(line2,2)
        lcd.text(str(line3),4)
        time.sleep(3)

        i=i+1
        if x==i:
            i=0
            run = False
     
