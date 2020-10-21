from client import Client
import json
import time
from monitor.usage_loger import Loger

file = open("config_experiments.json")
test_config = json.load(file)
file.close()

times = []

for i in range(test_config['n_arc']):
    start_time = time.time()
    new = Client(test_config["size_in_MB"])
    new.start()
    end_time = time.time()
    times.append(end_time-start_time)
    time.sleep(1/test_config['arc_per_sec'])
    newthread = Loger()
    newthread.start()

print("Response Time - {}".format(sum(times)/test_config['n_arc']))