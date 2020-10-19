from time import sleep
import psutil
from datetime import datetime 

file_log = open('./log_usage.csv', 'a')

while True:
    sleep(1)
    file_log.write(f'{psutil.cpu_percent()}, {psutil.virtual_memory().percent}, {datetime.now(tz=None)}\n')