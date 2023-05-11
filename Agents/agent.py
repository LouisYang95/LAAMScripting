#!/usr/bin/python3
import datetime
import time
import logging
import psutil

logging.basicConfig(level=logging.INFO,
                    filename="log.log",
                    filemode="a",
                    format='%(asctime)s - %(levelname)s - %(message)s')
# CPU INFOS
try:
    COUNT = 1

    # Loop infinite to print every 15 our info
    while True:
      # match:case condition to log everything in different interval depending the count
      if COUNT == 1 :
            print(datetime.datetime.now().time(),
                  psutil.cpu_times_percent(interval=0, percpu=False),
                  # logging.info(psutil.cpu_percent(interval=None, percpu=False)),
                  )
            logging.info(psutil.cpu_times_percent(interval=0, percpu=False))
                # logging.info(psutil.cpu_percent(interval=None, percpu=False))
            COUNT += 1
            time.sleep(10)
      elif COUNT == 2 :
            print(datetime.datetime.now().time(),
                  # psutil.virtual_memory(),
                  (psutil.virtual_memory().total - psutil.virtual_memory().available) / psutil.virtual_memory().total * 100)
            # logging.info(psutil.virtual_memory())
            logging.info((psutil.virtual_memory(
            ).total - psutil.virtual_memory().available) / psutil.virtual_memory().total * 100)
            COUNT += 1
            time.sleep(10)
      elif COUNT == 3 :
            print(datetime.datetime.now().time(),
                  psutil.disk_io_counters(perdisk=False, nowrap=True))
            logging.info(psutil.disk_io_counters(
                  perdisk=False, nowrap=True))
            COUNT += 1
            time.sleep(10)
      elif COUNT == 4 :
            print(datetime.datetime.now().time(), psutil.net_io_counters())
            logging.info(psutil.net_io_counters())
            COUNT = 1
            time.sleep(10)


except Exception as e:
    print(str(e).capitalize())
except KeyboardInterrupt:
    print("Finished")
