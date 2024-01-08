#!/usr/bin/python

import re
import subprocess

# Run the 'upower -d' command and capture the output
try:
    command_output = subprocess.check_output(["upower", "-d"], universal_newlines=True)
except subprocess.CalledProcessError as e:
    print("Error running 'upower -d'")
    exit(1)

# Define the regex pattern
pattern = re.compile(r"Device:.*?Roxcore.*?percentage:\s+(\d+)%\s*", re.DOTALL)

# Search for the pattern in the command output
match = pattern.search(command_output)

# If a match is found, print the battery percentage
if match:
    battery_percentage = match.group(1)
    print(battery_percentage + "%")
