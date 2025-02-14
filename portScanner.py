import os 
import re
import sys

# Get target from user 
if len(sys.argv) > 1:
    target = sys.argv[1]
else: 
    print("No target provided")
    sys.exit(1)  # Exit if no target is provided

# Create the filename
file = f"ScanResults.txt"

# Create an empty list for addresses 
addresses = []

# -sn scan for live host discovery
os.system(f"nmap -sn {target} -oN {file}")  

# RegEx to filter for live hosts
with open(file, "r") as resultsFile:
    lines = resultsFile.read()  # Read entire file content
    addresses = re.findall(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", lines)  # Extract IPs

# Write filtered addresses to a file
with open("filteredAddresses.txt", "w") as fResults:
    for address in addresses:
        fResults.write("Results From Host Discovery: \n")
        fResults.write(address + "\n")


# Perform a stealth scan 
os.system(f"nmap -sS -p- -iL {fResults}")