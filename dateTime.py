from rpi_lcd import LCD
from datetime import datetime, date

lcd - LCD()

def show_date_time():
    d4 = date.today().strftime("%b-%d-%Y")
    current_time = datetime.now().strftime("%I:%M")
    lcd.text(current_time,2,'center')
    lcd.text(d4,3,'center')