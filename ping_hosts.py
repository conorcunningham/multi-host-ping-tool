import os
import asyncio
from pathlib import Path
from multi_host_ping_tool.ping_and_log import ping_and_log

hosts_file = Path("data/hosts")

if not os.path.isfile(hosts_file):
    if not os.path.isdir("data"):
        os.mkdir("data")
    Path(hosts_file).touch()


async def queue_tasks(queue) -> None:
    """
    This coroutine will read the hosts file and put each host in the queue.
    In a Python queue example, this would be the producer
    All we are doing here is adding a host (an IP address) to the queue
    :param queue:
    :return: None
    """
    for host in read_hosts():
        await queue.put(host)
    await queue.put(None)


def read_hosts() -> list:
    """
    This function will read the hosts file and return a list of hosts
    It expects the hosts file to contain a single IP address per line
    e.g.,
    192.168.1.100
    192.168.2.100
    192.168.3.100
    :return: Lists of IP addresses
    """
    with open(hosts_file, "r") as infile:
        hosts = infile.readlines()
        hosts = [host.strip() for host in hosts if host is not None]
    return hosts


# coroutine to consume work
async def consumer(queue) -> None:
    """
    Pull hosts from the queue and send them to ping_and_log
    :param queue:
    :return: None
    """
    print('Ping tasks: Running')
    # consume work
    while True:
        # get a unit of work
        host = await queue.get()
        # check for stop signal
        if host is None:
            break
        # pass hosts to the ping test method
        await ping_and_log(host)
    print('Ping Tasks: Done. Check log file for results')


async def main() -> None:
    # create the shared queue
    queue = asyncio.Queue(maxsize=30)
    # run the producer and consumers
    await asyncio.gather(queue_tasks(queue), consumer(queue))


if __name__ == "__main__":
    asyncio.run(main())
