from Adafruit_CharLCD import Adafruit_CharLCD

lcd = Adafruit_CharLCD(25,24,23,17,18,22,16,2,4)
lcd.clear()

def lcd_temp(temperature):
        lcd.clear()
        lcd.message('{} C'.format(temperature))
