import psutil
import datetime
import time
import logging

temps = 1
max_temps = 4

count = 1

while count < max_temps:
    print(datetime.datetime.now().time(),
          psutil.cpu_times_percent(interval=1))
    time.sleep(temps)
    count += 1

logging.basicConfig(level=logging.DEBUG,
                    filename="log.log",
                    filemode="a",
                    format='%(asctime)s - %(levelname)s - %(message)s')


logging.info(psutil.cpu_times_percent(interval=1))