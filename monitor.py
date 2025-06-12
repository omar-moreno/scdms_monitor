import logging
import subprocess
import time

from logfmter import Logfmter

handler = logging.StreamHandler()
handler.setFormatter(Logfmter())

logging.basicConfig(level=logging.INFO, handlers=[handler])

def check_disk():
    output = subprocess.run(
            ["df", "-h", "/sdf/data/supercdms"],
            stdout=subprocess.PIPE,
            )
    output = output.stdout.split()
    total_size = output[8].decode("utf-8")[:-1]
    used = output[9].decode("utf-8")[:-1]
    percent = output[11].decode("utf-8")[:-1]
    logging.info("", extra={"total_size": total_size, "used": used, "percent": percent})

if __name__ == '__main__':
    while True:
        check_disk()
        time.sleep(60)
