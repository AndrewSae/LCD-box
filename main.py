import time
from webbrowser import get
from gpiozero import Button
from rpi_lcd import LCD
import sendMeme as meme
import dateTime as home
import stockInfo as stock

btn1 = Button(24)
btn2 = Button(23)
btn3 = Button(18)
lcd = LCD()


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
        stock.show()
        lcd.clear()
    else:
        home.show()
