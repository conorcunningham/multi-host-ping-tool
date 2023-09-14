import os.path
import logging
from icmplib import async_multiping
from pathlib import Path


log_file = Path("logs/icmp_results.log")

if not os.path.isfile(log_file):
    if not os.path.isdir("logs"):
        os.mkdir("logs")
    Path(log_file).touch()


# Create a custom logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Create handlers
stream_handler = logging.StreamHandler()
file_handler = logging.FileHandler(log_file)
stream_handler.setLevel(logging.INFO)
file_handler.setLevel(logging.INFO)

# Create formatters and add it to handlers
stream_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
# file_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_format = logging.Formatter('%(asctime)s - %(message)s')

stream_handler.setFormatter(stream_format)
file_handler.setFormatter(file_format)

# Add handlers to the logger
logger.addHandler(stream_handler)
logger.addHandler(file_handler)


async def ping_and_log(hosts, count=1, privileged=False):
    results = await async_multiping(hosts, count=count, privileged=privileged)
    parse_result(results)
    return results


def parse_result(results) -> None:
    for result in results:
        if result.is_alive:
            logger.info(f"{result.address} is alive")
        else:
            logger.error(f"FAILURE: {result.address} is NOT alive")
