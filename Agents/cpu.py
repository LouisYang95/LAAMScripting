import psutil
import datetime
import time
import logging

temps = 1
max_temps = 1

count = 1

logging.basicConfig(level=logging.INFO,
                    filename="log.log",
                    filemode="a",
                    format='%(asctime)s - %(levelname)s - %(message)s')

while count < max_temps:
    print(datetime.datetime.now().time(),
          logging.info(psutil.cpu_times_percent(interval=1)))
    time.sleep(temps)
    count += 1

print(psutil.virtual_memory())
print(psutil.cpu_stats())
