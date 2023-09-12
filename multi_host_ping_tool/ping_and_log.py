import logging
from icmplib import ping
from pathlib import Path


log_file = Path("logs/icmp_results.log")

# Create a custom logger
logging.basicConfig()
logger = logging.getLogger(__name__)

# Create handlers
stream_handler = logging.StreamHandler()
file_handler = logging.FileHandler(log_file)
stream_handler.setLevel(logging.DEBUG)
file_handler.setLevel(logging.DEBUG)
# logging.basicConfig(level=logging.INFO, format='%(message)s')

# Create formatters and add it to handlers
stream_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
# file_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_format = logging.Formatter('%(asctime)s - %(message)s')
stream_handler.setFormatter(stream_format)
file_handler.setFormatter(file_format)

# Add handlers to the logger
logger.addHandler(stream_handler)
logger.addHandler(file_handler)


async def ping_and_log(host):
    ping_result = ping(host, count=1, privileged=False)
    await parse_result(ping_result)
    return ping_result


async def parse_result(result):
    if result.is_alive:
        logger.info(f"{result.address} is alive")
    else:
        logger.error(f"{result.address} is NOT alive")
