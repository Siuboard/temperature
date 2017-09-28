import get_temperature
import lcd_temp
from xml_class import Xml_File

class Temperature:
    minimal, maximal = None, None

    @classmethod
    def main(cls):
        temperature = get_temperature.get_temp()
        
        if not cls.minimal:
            Xml_File.value_compare(temperature)
            cls.minimal, cls.maximal = float(Xml_File.minimal), float(Xml_File.maximal)

        elif temperature > cls.maximal:
            cls.maximal = temperature
            Xml_File.value_compare(temperature)

        elif temperature < cls.minimal:
            cls.minimal = temperature
            Xml_File.value_compare(temperature)
                    
        lcd_temp.lcd_temp(temperature)

if __name__ == '__main__':
    while True:
        Temperature().main()
