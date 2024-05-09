import socket
from concurrent.futures import ThreadPoolExecutor

common_ports = {
    20: "FTP Data",
    21: "FTP Control",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    443: "HTTPS",
    143: "IMAP",
    161: "SNMP",
    194: "IRC",
    389: "LDAP",
    443: "HTTPS",
    445: "SMB",
    465: "SMTPS",
    514: "Syslog",
    587: "SMTP",
    636: "LDAPS",
    993: "IMAPS",
    995: "POP3S",
    1080: "Proxy",
    1433: "MSSQL",
    1521: "Oracle",
    3306: "MySQL",
    3389: "RDP",
    5432: "PostgreSQL",
    5900: "VNC",
    6379: "Redis",
    8000: "HTTP Alternate",
    8080: "HTTP Alternate",
    8443: "HTTPS Alternate",
}

def scan_port(target_ip, port):
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = client_socket.connect_ex((target_ip, port))
        if result == 0:
            service = common_ports.get(port, "Bilinmeyen servis")
            print(f"Port {port} ({service}): Açık")
        client_socket.close()
    except Exception as e:
        print(f"Hata: {e}")

def port_scan(target_ip):
    target_ports = range(1, 1001)
    with ThreadPoolExecutor(max_workers=50) as executor:
        executor.map(lambda port: scan_port(target_ip, port), target_ports)

target_ip = input("Hedef IP adresini girin: ")

port_scan(target_ip)

