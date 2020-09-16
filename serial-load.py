import serial
import time
from datetime import datetime

MESSAGE = 'I love scotch. Scotchy scotch scotch. Here it goes down, down into my belly.'

with serial.Serial('/dev/rfcomm0', 115200) as ser:
    count = 0
    while True:
        stamped_message = '{}: {}, {}'.format(datetime.now(), MESSAGE, count)
        ser.write(stamped_message.encode('utf-8'))
        while ser.in_waiting < 1:
            time.sleep(0.001)
        response = ser.read_all()
        if count % 100 == 0:
            print(response)
        count = count + 1
