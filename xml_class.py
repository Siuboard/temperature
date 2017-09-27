import os
import xml.etree.ElementTree as et
import time

class Xml_File:
    
    base_path = os.path.dirname(os.path.realpath(__file__))
    data_dir = os.path.join(base_path, 'data')

    if not os.path.exists(data_dir):
        os.mkdir(data_dir)
        
    xml_file = os.path.join(base_path, 'data/day_b_day.xml')

    root = None
    tree = None
    minimal = None
    maximal = None

    @classmethod
    def get_date(cls):
        return time.strftime('%d.%m.%Y')

    @classmethod
    def xml_parse(cls):
        date = cls.get_date()
        
        if not os.path.exists(cls.xml_file):
            with open(cls.xml_file, 'a+') as f:
                cls.root = et.Element('days')
                cls.tree = et.ElementTree(cls.root)
                cls.new_day_record(date)
                
        cls.tree = et.parse(cls.xml_file)
        cls.root = cls.tree.getroot()
        if cls.root.find('day[last()]').get('date') != date:
            cls.new_day_record(date)
            

    @classmethod
    def new_day_record(cls, date):
        new_day = et.SubElement(cls.root, 'day', {'date' : date,
                                                  'min_temp': '',
                                                  'max_temp': ''}
                                                  )
        cls.tree.write(cls.xml_file)

    @classmethod
    def value_compare(cls, temperature):
        cls.xml_parse()
        last_day = cls.root.find('day[last()]')
        cls.minimal = last_day.get('min_temp')
        cls.maximal = last_day.get('max_temp')
        
        if not cls.minimal:
            cls.minimal, cls.maximal = temperature, temperature
            last_day.set('min_temp', str(temperature))
            last_day.set('max_temp', str(temperature))
            
        elif float(cls.minimal) > float(temperature):
            last_day.set('min_temp', str(temperature))

        elif float(cls.maximal) < float(temperature):
            last_day.set('max_temp', str(temperature))

        cls.tree.write(cls.xml_file)


