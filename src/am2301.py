
import subprocess
import json
import datetime

def read_am2301():

    cmd = list()
    cmd = ["../raspberry_pi_DHT21-AM2301/src/am2301/am2301"]
    exec_return = subprocess.run(cmd)

    if exec_return.returncode == 0:
        json_data = json.loads(exec_return.stdout)
        current_dt = datetime.datetime.now()
        print(f"{current_dt}:{json_data}")

if __name__ == "__main__":
    read_am2301()