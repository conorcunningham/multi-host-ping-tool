# multi-host-ping-tool

## Description
Use this tool to ping multiple hosts at once. The tool will ping each host in the hosts file and return the results in a text log file.

It utilises asycnio to speed up the process of pinging multiple hosts. If all hosts respond to ICMP, the program will execute very quickly. Hosts not responding to ICMP request packets will take a little longer to complete.

## Hosts file
The program will look for `./data/hosts` by default. The hosts file must contain a single host per line. A host can be defined by a FQDN or IP address. If the file and/or directory do not exist, the program will create them.

Here is an example hosts file:
```text
192.168.1.100
192.168.2.200
10.47.99.12
www.google.com
```

## Log file

The log will be stored at `.log/icmp_results.log`. If this file and/or directory do not exist, the program will create them

The log format is as follows:
```text
2023-09-12 20:48:39,992 - 10.48.219.1 is alive
2023-09-12 20:48:41,993 - 10.46.150.42 is NOT alive
```

## Usage
```bash
python multi_host_ping_tool.py 
```

## Requirements
* Python 3.6+
* icmplib
Install requirements with pip
```bash
pip install -r requirements.txt
```

Install icmplib with pip
```bash
pip install icmplib
```

### Happy Pinging

## Author
Conor Cunningham