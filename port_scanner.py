import socket
from datetime import datetime

def scan_ports(target, port_range):
    # Starting time
    start_time = datetime.now()
    print(f"Starting scan on {target} at {start_time}")

    # Loop through ports in the given range
    for port in port_range:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        
        # Try to connect to the target on the given port
        result = sock.connect_ex((target, port))
        
        if result == 0:
            print(f"Port {port}: OPEN")
        sock.close()

    # Ending time
    end_time = datetime.now()
    print(f"Scan completed in {end_time - start_time}")

if __name__ == "__main__":
    target = input("Enter the IP address or hostname to scan: ")
    port_range = range(1, 6000) 
    
    scan_ports(target, port_range)
