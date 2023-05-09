import psutil
import datetime
import time

temps = 1
max_temps = 5

count = 1

while count < max_temps:
    print(datetime.datetime.now().time(),
          psutil.cpu_times_percent(interval=1))
    time.sleep(temps)
    count += 1