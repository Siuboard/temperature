import os
import glob
import time


base_dir = "/sys/bus/w1/devices/"
device_dir = glob.glob(base_dir + '28*')[0]
device_file = device_dir + '/w1_slave'


def get_temp_from_file():
    
    with open(device_file, 'r') as f:
        lines = f.readlines()

    return lines

def get_temp():
    lines = get_temp_from_file()

    while lines[0].strip()[-3:] != "YES":
        time.sleep(0.2)
        get_temp_from_file()

    equals_sign_pos = lines[1].find('t=')

    if equals_sign_pos != -1:
        temp_string = lines[1][equals_sign_pos + 2:]
        temp_c = float(temp_string) / 1000.0
        return round(temp_c, 2)        
    

if __name__ == "__main__":

    for i in range(10):
        print(get_temp())
        time.sleep(2)

