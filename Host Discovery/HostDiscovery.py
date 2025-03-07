import re
import sys
import subprocess

# Get target from user
if len(sys.argv) > 1:
    target = sys.argv[1]
else:
    print("No target provided")
    sys.exit(1)  # Exit if no target is provided

# Create the filename
file = "DiscoveredHosts.txt"

# Run nmap with -sn scan for live host discovery
subprocess.run(["nmap", "-sn", target, "-oN", file], check=True)

# RegEx to filter for live hosts
addresses = []

with open(file, "r") as f:
    lines = f.read()  # Read entire file content
    addresses = re.findall(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", lines)  # Extract IPs

# Write the extracted IPs to the file
with open(file, "w") as f:
    for address in addresses:
        f.write(address + "\n")

print(f"Live hosts saved to {file}")