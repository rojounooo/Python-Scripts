# Script Overview

## Purpose

This script will send requests to a target website to attempt directory bruteforcing using common directory names such as admin. 


## Usage
- Download the script 
- In the terminal change to the directory containing the script
- Run the following command
```bash
python DirectoryBruteForce.py {target_url}
```


# How it works

## 1. Check for Target  
- The script first checks if a target has been provided as an argument.  

## 2. Create Output File  
- If a target is provided, a file is created to store the results 

## 3. Send requests
- The script will start creating requests using words from the directory list

## 4. Append to file 
- The file will be opened and only URLS which returned a status code of 200 will be appended to the file for later use.

