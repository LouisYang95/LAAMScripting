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
      while True:
          match count:
              case 1:
                  print(datetime.datetime.now().time(),
                        psutil.cpu_times_percent(interval=0, percpu=True),
                        )
                  logging.info(psutil.cpu_times_percent(interval=0))
                  count += 1
                  time.sleep(10)
              case 2:
                  print(datetime.datetime.now().time(),
                        psutil.virtual_memory(),
                        )
                  logging.info(psutil.virtual_memory())
                  count += 1
                  time.sleep(10)
              case 3:
                  print(datetime.datetime.now().time(),
                        psutil.disk_io_counters(perdisk=False, nowrap=True)
                        )
                  logging.info(psutil.disk_io_counters(perdisk=False, nowrap=True))
                  count += 1
                  time.sleep(10)


except Exception as e:
      print (str(e).capitalize())
except KeyboardInterrupt:
      print ("Finished")
