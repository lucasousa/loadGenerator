from time import sleep
import psutil
from datetime import datetime 
import threading

class Loger():
    def __init__(self, infos):
        self.exp_infos = infos
        self.log_arc = "./monitor/log_usage.csv"
        self.file_log = None

    def start(self):
        self.file_log = open(self.log_arc)
        print("[loger] started loger")
        sleep(1)
        self.file_log.write(f"{psutil.cpu_percent()},{psutil.virtual_memory().percent},{self.exp_infos['n_arc']},{self.exp_infos['size_in_MB']},{self.exp_infos['arc_per_sec']},{datetime.now(tz=None)}\n")
        self.file_log.close()
        print("[loger] file closed")
    