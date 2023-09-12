import os
import asyncio
from pathlib import Path
from multi_host_ping_tool.ping_and_log import ping_and_log

hosts_file = Path("data/hosts")

if not os.path.isfile(hosts_file):
    if not os.path.isdir("data"):
        os.mkdir("data")
    Path(hosts_file).touch()


async def queue_tasks(queue):
    # tasks = []
    for host in read_hosts():
        await queue.put(host)
        # tasks.append(ping_and_log(host))
    await queue.put(None)
    # await asyncio.gather(*tasks)


def read_hosts():
    with open(hosts_file, "r") as infile:
        hosts = infile.readlines()
        hosts = [host.strip() for host in hosts if host is not None]
    return hosts


# coroutine to consume work
async def consumer(queue):
    print('Consumer: Running')
    # consume work
    while True:
        # get a unit of work
        host = await queue.get()
        # check for stop signal
        if host is None:
            break
        # report
        await ping_and_log(host)
    # all done
    print('Consumer: Done')


async def main():
    # create the shared queue
    queue = asyncio.Queue(maxsize=30)
    # run the producer and consumers
    await asyncio.gather(queue_tasks(queue), consumer(queue))


# if __name__ == "__main__":
asyncio.run(main())
