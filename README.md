# Simple Port Scanner

## Overview
This project is a simple port scanner written in Python. The scanner allows you to check which ports are open on a specified target IP address or hostname. It's a useful tool for network troubleshooting and basic security assessments.

## Features
- Scans a range of ports (default: 1 to 1024).
- Detects and lists open ports.
- Simple and easy to use.
- Displays the total time taken for the scan.

## Prerequisites
- **Python 3.x**: Ensure Python is installed on your system. You can download it from [python.org](https://www.python.org/).

## Installation
1. **Clone the repository** (if this were part of a repository):
   ```bash
   git clone https://github.com/Aditya19Joshi01/SimplePortScanner.git
   cd simple-port-scanner
2. **Run the script**: No special dependencies are required. Simply run the script using Python.
    ```bash
    python port_scanner.py

## Customization
Change Port Range: Modify the port_range in the script to scan different ports.
Timeout Settings: Adjust the socket.setdefaulttimeout(1) to change the connection timeout period.
