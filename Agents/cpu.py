import psutil
import datetime
import time
import logging

logging.basicConfig(level=logging.INFO,
                    filename="log.log",
                    filemode="a",
                    format='%(asctime)s - %(levelname)s - %(message)s')

try:    
      while True:
            print(datetime.datetime.now().time(),
            psutil.cpu_times_percent(interval=0, percpu=True),
            )
            logging.info(psutil.cpu_times_percent(interval=0))
            time.sleep(10)
except Exception as e:
      print (str(e).capitalize())
except KeyboardInterrupt:
      print ("Finished")
