# Script Overview
---
## Purpose

This script will attempt live host discovery using nmap with the -sn scan and then parse the results to leave only the IP addresses that were up.

This scan works by sending 4 different types of packets without doing a port scan:
- ICMP Echo Request (ping)
- TCP SYN packet to port 443
- TCP ACK packet to port 80
- ICMP Timestamp request
--- 


## Usage 
 - Download the script 
 - In the terminal change to the directory containing the script
 - Run the following command 
 ```bash 
 python3 HostDiscovery.py {target address/range}
```

# How it works 

## 1. Check for Target  
- The script first checks if a target has been provided as an argument.  

## 2. Create Output File  
- If a target is provided, a file is created to store the scan results.  

## 3. Run the Scan  
- The script executes a scan and saves the output to `DiscoveredHosts.txt`.  

## 4. Parse Results  
- The script opens and reads the output file.  
- It extracts only the IP addresses of hosts that are up and stores them in a list.  

## 5. Overwrite Output File  
- The script writes the filtered IP addresses back to `DiscoveredHosts.txt`, overwriting its previous contents.  
