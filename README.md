# Brute Force Detection Tool

## Overview
This Python-based tool analyzes authentication logs to detect potential brute force attacks by identifying repeated failed login attempts from the same IP address.

## Features
- Parses log files for failed login attempts
- Counts occurrences by IP address
- Flags suspicious IPs based on a configurable threshold
- Sorts results by highest failed attempts
- Generates a timestamped report of suspicious activity

## Example Output
IP: 192.168.1.10 | Failed Attempts: 3
IP: 10.0.0.5 | Failed Attempts: 3

## How to Run
1. Place your log file in the project folder
2. Run: python detector.py
3. View results in report.txt

## Skills Demonstrated
- Log analysis
- Threat detection (brute force attacks)
- Python scripting and automation
- Security-focused problem solving
