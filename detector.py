# Brute Force Detection Tool
# Analyzes login logs to detect repeated failed attempts from the same IP

from datetime import datetime

ip_counts = {}

# Read log file
with open("log.txt", "r") as file:
    for line in file:
        if "Failed" in line:
            parts = line.split("IP: ")
            ip = parts[1].strip()

            if ip in ip_counts:
                ip_counts[ip] += 1
            else:
                ip_counts[ip] = 1

# Set detection threshold
threshold = 2

# Sort IPs by highest failed attempts
sorted_ips = sorted(ip_counts.items(), key=lambda x: x[1], reverse=True)

# Write results to report
with open("report.txt", "w") as report:
    report.write("=== Brute Force Detection Report ===\n")
    report.write(f"Generated on: {datetime.now()}\n\n")

    for ip, count in sorted_ips:
        if count >= threshold:
            report.write(f"IP: {ip} | Failed Attempts: {count}\n")

print("Report generated: report.txt")