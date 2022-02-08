from datetime import datetime, date
from rpi_lcd import LCD

lcd = LCD()



def show():
    d4 = date.today().strftime("%b-%d-%Y")
    current_time = datetime.now().strftime("%I:%M")
    lcd.text(current_time,2,'center')
    lcd.text(d4,3,'center')
  

