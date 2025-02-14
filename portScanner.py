import os 
import re
import sys

# Get target from user 
if len(sys.argv) > 1:
    target = sys.argv[1]
    file = f"{target}ScanResults"
else: 
    print("No target provided")
    sys.exit(1)  # Exit if no target is provided

# Create an empty list for addresses 
addresses = []

# -sn scan for live host discovery
os.system(f"nmap -sN {target} -oN {file}")  

# RegEx to filter for live hosts
with open(file, "r") as resultsFile:
    lines = resultsFile.read()  # Read entire file content
    addresses = re.findall(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", lines)  # Extract IPs

# Write filtered addresses to a file
with open("filteredResults.txt", "w") as fResults:
    for address in addresses:
        fResults.write(address + "\n")
