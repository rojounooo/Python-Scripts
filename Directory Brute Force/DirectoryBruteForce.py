import sys
import subprocess
import requests

# Get target from user
if len(sys.argv) > 1:
    target = sys.argv[1]
else:
    print("No target provided")
    sys.exit(1)  # Exit if no target is provided

# Create the filename
file = "foundDirecrories.txt"

#  List of common directories 
dir_list = ["admin", "news", "index", "images", "login", "contact"]

for word in dir_list: # Loop through the list of directories
    url = f"{target}/{word}" # Create the URL
    response = requests.get(url) # Send the request
    if response.status_code == 200: # Check if the response is OK
        print(f"[+] Discovered directory: {url}") # Print the discovered directory
        with open(file, "a") as f: # Append the discovered directory to the file
            f.write(url + "\n") # Write the URL to the file

