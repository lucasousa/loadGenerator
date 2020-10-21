from client import Client
import json
import time

file = open("config_experiments.json")
test_config = json.load(file)
file.close()

times = []

for i in range(test_config['n_arc']):
    
    new = Client(test_config["size_in_MB"])
    new.start()

    # times.append(end_time-start_time)
    time.sleep(1/test_config['arc_per_sec'])

# print("Response Time - {}".format(sum(times)/test_config['n_arc']))