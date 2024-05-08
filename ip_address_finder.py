import socket

def find_ip_address(domain):
    try:
        ip_address = socket.gethostbyname(domain)
        return ip_address
    except socket.gaierror:
        return "IP adresi bulunamadı."

if __name__ == "__main__":
    domain_name = input("Alan adını girin: ")
    ip_address = find_ip_address(domain_name)
    print("Alan adı:", domain_name)
    print("IP adresi:", ip_address)
