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
    total_size = output.stdout[71:-39].decode("utf-8")
    used = output.stdout[77:-33].decode("utf-8")
    percent = output.stdout[ 88:-22].decode("utf-8")
    logging.info("", extra={"total_size": total_size, "used": used, "percent": percent})

if __name__ == '__main__':
    while True:
        check_disk()
        time.sleep(60)
