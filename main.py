import socket
import sys
from datetime import datetime

def scan_ports(target_host, ports_to_scan):
    print("-" * 50)
    print(f"Scanning Target: {target_host}")
    print(f"Time Started: {str(datetime.now())}")
    print("-" * 50)
    
    try:
        # Loop through each port specified in our list
        for port in ports_to_scan:
            # AF_INET specifies IPv4, SOCK_STREAM specifies TCP
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            
            # Set a timeout so the script doesn't hang forever on a closed port
            s.settimeout(1.0)
            
            # attempt to connect to the target IP and port
            result = s.connect_ex((target_host, port))
            
            # connect_ex returns 0 if the connection was successful
            if result == 0:
                print(f"Port {port}: OPEN")
            else:
                # Optional: uncomment the line below if you want to see closed ports too
                # print(f"Port {port}: Closed")
                pass
                
            # Always close the socket connection
            s.close()
            
    except KeyboardInterrupt:
        print("\nExiting script cleaner via user interrupt.")
        sys.exit()
        
    except socket.gaierror:
        print("\nHostname could not be resolved.")
        sys.exit()
        
    except socket.error:
        print("\nCould not connect to server.")
        sys.exit()

if __name__ == "__main__":
    # Test target: 'scanme.nmap.org' is a safe, legal server provided by Nmap for testing
    target = "scanme.nmap.org"
    
    # Common ports to check: 22 (SSH), 80 (HTTP), 443 (HTTPS)
    ports = [21, 22, 80, 139, 443, 8080]
    
    scan_ports(target, ports)
