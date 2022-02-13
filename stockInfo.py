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

def show():
    x = len(tickers)
    i =0
    run=True
    while run:
        ticker = yf.Ticker(tickers[i])
        
        current_price = get_current_price(ticker)
        last_close = get_last_close(ticker)
        percent_change =((current_price - last_close)/last_close)*100
                
        format_current_price = format(current_price, ",.2f")
        format_percent_change = format(percent_change, ",.2f")
        
        
        line1 =  tickers[i] + '(' + ticker_comp_names[i] + ')'
        line2 = "price: " + "$" + format_current_price
        
        if percent_change>0:
            line3 = "+" + format_percent_change + "% up today"
        else:
            line3 = format_percent_change + "% down today"

        
        lcd.clear()
        lcd.text(line1,1)
        lcd.text(line2,2)
        lcd.text(str(line3),4)
        time.sleep(3)
        i=i+1
        if x==i:
            i=0
            run = False
     
