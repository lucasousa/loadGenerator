from time import sleep
import psutil
from datetime import datetime 
import threading

class Loger(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.log_arc = "./monitor/log_usage.csv"
        self.file_log = None

    def run(self):
        self.file_log = open(self.log_arc, "a")
        sleep(1)
        self.file_log.write(f"{psutil.cpu_percent()},{psutil.virtual_memory().percent},{datetime.now(tz=None)}\n")
        self.file_log.close()

 