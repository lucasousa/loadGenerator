from time import sleep
import psutil
from datetime import datetime 
import threading

class Loger(threading.Thread):
    def __init__(self, process):
        threading.Thread.__init__(self)
        self.process = process
        self.log_arc = "./monitor/log_usage.csv"
        self.file_log = None
        self.read = True

    def run(self):
        self.file_log = open(self.log_arc, "a")
        while self.read:
            sleep(1)
            self.file_log.write(f"{self.process.cpu_percent()},{(self.process.memory_info().vms/psutil.virtual_memory().total)*100:.2f},{datetime.now(tz=None)}\n")
        self.file_log.close()

    def stop(self):
        self.read = False

 