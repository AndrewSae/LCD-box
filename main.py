import time
from webbrowser import get
from gpiozero import Button
from rpi_lcd import LCD
from datetime import datetime, date
import yfinance as yf
import sendMeme as meme

btn1 = Button(24)
btn2 = Button(23)
btn3 = Button(18)
lcd = LCD()

tickers = ["AAPL", "AMZN", "MSFT", "TSLA"]
ticker_comp_names = ["Apple", "Amazon", "Microsoft", "Tesla"]

def show_date_time():
    d4 = date.today().strftime("%b-%d-%Y")
    current_time = datetime.now().strftime("%I:%M")
    lcd.text(current_time,2,'center')
    lcd.text(d4,3,'center')


def get_current_price(ticker):
    todays_data = ticker.history(period='1d')
    price=  todays_data['Close'][0]
    return price

def get_last_close(ticker):
    todays_data = ticker.history(period='5d')
    price=  todays_data['Close'][3]
    return price
def get_first_stock_info():
    ticker = yf.Ticker(tickers[0])
    first_last_close = get_last_close(ticker)
    first_current_price = get_current_price(ticker)
    first_percent_change = ((first_current_price - first_last_close)/first_last_close)*100  
def show_first(current_price,percent_change):
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



def show_stock():
    show_first(first_current_price,first_percent_change)
    x = len(tickers)
    i =1
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

while True:
    if btn1.is_pressed == False:
        lcd.clear()
        lcd.text('sending...',2,'center')
        meme.sendMeme()
        time.sleep(2)
        lcd.clear()
        lcd.text(' meme sent :)',2,'center')
        time.sleep(2)
    elif btn2.is_pressed == False:
        show_stock()
        lcd.clear()
    else:
        show_date_time()
        get_first_stock_info
