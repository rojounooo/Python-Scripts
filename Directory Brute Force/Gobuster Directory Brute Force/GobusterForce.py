import re 
import sys
import subprocess

# Get target website and wordlist from user
if len(sys.argv) == 2:
    target = sys.argv[1]
    wordlist = sys.argv[2]
else:
    print("Either no target or wordlist provided")
    sys.exit(1)  # Exit if no target or wordlist is provided

# Create the filename
file = "FoundDirectories.txt"

# Command to run 
subprocess.run(["gobuster", "dir", "-u", target, "-w", wordlist, ">>", file], check=True)

