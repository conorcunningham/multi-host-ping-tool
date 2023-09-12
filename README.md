# multi-host-ping-tool

## Description
Use this tool to ping multiple hosts at once. The tool will ping each host in the hosts file and return the results in a text log file.

It utilises asycnio to speed up the process of pinging multiple hosts. If all hosts respond to ICMP, the program will execute very quickly. Hosts not responding to ICMP request packets will take a little longer to complete.

## Hosts file
The program will look for `./data/hosts` by default. The hosts file must contain a single host per line. A host can be defined by a FQDN or IP address. If the file and/or directory do not exist, the program will create them.

The log will be stored at `.log/icmp_results.log`. If this file and/or directory do not exist, the program will create them

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