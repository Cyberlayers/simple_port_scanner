import socket  # Import the socket module for network connections

def scan_port(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Create a TCP socket
    sock.settimeout(1)  # Set timeout to avoid long waits on closed ports
    result = sock.connect_ex((ip, port))  # Attempt to connect to the port
    if result == 0:
        print(f"Port {port} is open")
    else:
        print(f"Port {port} is closed")
    sock.close()  # Close the socket

if __name__ == "__main__":
    target_ip = input("Enter the target IP address: ")
    port_range = input("Enter port range (e.g., 20-25): ")
    start_port, end_port = map(int, port_range.split('-'))

    print(f"Scanning ports {start_port} to {end_port} on {target_ip}")
    for port in range(start_port, end_port + 1):
        scan_port(target_ip, port)
