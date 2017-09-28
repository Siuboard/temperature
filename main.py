import get_temperature
import lcd_temp
#import xml_up
import xml_class

class Temperature:
    minimal, maximal = None, None

    @classmethod
    def main(cls):
        temperature = get_temperature.get_temp()
        
        if not cls.minimal:
            xml_class.Xml_File.value_compare(temperature)
            cls.minimal, cls.maximal = float(xml_class.Xml_File.minimal), float(xml_class.Xml_File.maximal)
            #xml_up.value_compare(temperature)
        elif temperature > cls.maximal:
            cls.maximal = temperature
            xml_class.Xml_File.value_compare(temperature)
            #xml_up.value_compare(temperature)
        elif temperature < cls.minimal:
            cls.minimal = temperature
            xml_class.Xml_File.value_compare(temperature)
            #xml_up.value_compare(temperature)
            
        lcd_temp.lcd_temp(temperature)

if __name__ == '__main__':
    while True:
        Temperature().main()
