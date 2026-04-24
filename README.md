# Brute Force Detection Tool

## Overview
This project analyzes authentication logs to detect potential brute force attacks by identifying repeated failed login attempts from the same IP address.

## Features
- Parses log files for failed login attempts
- Counts occurrences by IP address
- Flags suspicious IPs based on a threshold
- Generates a report of suspicious activity

## Example Output
IP: 192.168.1.10 | Failed Attempts: 5

## How to Run
1. Place your log file in the project folder
2. Run: python detector.py
3. View results in report.txt

## Skills Demonstrated
- Log analysis
- Basic threat detection
- Python scripting
- Security-focused problem solving
