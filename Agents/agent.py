import datetime as datetime
import psutil
import datetime
import time
import logging

logging.basicConfig(level=logging.INFO,
                    filename="log.log",
                    filemode="a",
                    format='%(asctime)s - %(levelname)s - %(message)s')

count = 1

#CPU INFOS
try:
      # Loop infinite to print every 15 our info
      while True:
          match count: # match:case condition to log everything in different interval depending the count
              case 1:
                  print(datetime.datetime.now().time(),
                        psutil.cpu_times_percent(interval=0, percpu=False),
                        # logging.info(psutil.cpu_percent(interval=None, percpu=False)),
                        )
                  logging.info(psutil.cpu_times_percent(interval=0, percpu=False))
                  # logging.info(psutil.cpu_percent(interval=None, percpu=False))
                  count += 1
                  time.sleep(10)
              case 2:
                  print(datetime.datetime.now().time(),
                        # psutil.virtual_memory(),
                        (psutil.virtual_memory().total - psutil.virtual_memory().available) / psutil.virtual_memory().total * 100
                        )
                  # logging.info(psutil.virtual_memory())
                  logging.info((psutil.virtual_memory().total - psutil.virtual_memory().available) / psutil.virtual_memory().total * 100)
                  count += 1
                  time.sleep(10)
              case 3:
                  print(datetime.datetime.now().time(),
                        psutil.disk_io_counters(perdisk=False, nowrap=True)
                        )
                  logging.info(psutil.disk_io_counters(perdisk=False, nowrap=True))
                  count = 1
                  time.sleep(10)


except Exception as e:
      print (str(e).capitalize())
except KeyboardInterrupt:
      print ("Finished")
