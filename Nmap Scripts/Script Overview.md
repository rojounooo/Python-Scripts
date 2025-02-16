# Script Overview
---
## Whats the point of this script 

This script will take attempt live host discovery using nmap with the -sn scan and then parse the results to leave only the IP addresses that were up.

This scan works by sending 4 different types of packets without doing a port scan:
- ICMP Echo Request (ping)
- TCP SYN packet to port 443
- TCP ACK packet to port 80
- ICMP Timestamp request
--- 

## When does it work 
This script will work when the network is directly reachable, for example when you're connected to your home network.

It will not always work for a public network due to firewall restrictions such as:
- Blocking pings
- Blocking Nmap TCP probes 
---

## How to run the script 
 - Download the script 
 - In the terminal change to the directory containing the script
 - Run the following command 
 ```bash 
 python3 HostDiscovery.py {target address/range}
```

## How does the script work 