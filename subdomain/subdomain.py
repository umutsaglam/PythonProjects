# CTI Academy Task 11
# Umut Sağlam

import socket
import requests
import argparse

def subdomain_brute_force(domain, wordlist_file):
    subdomains = []
    with open(wordlist_file, 'r') as file:
        for line in file:
            subdomain = line.strip() + "." + domain
            try:
                # IP adresi çözümlemesi
                ip_address = socket.gethostbyname(subdomain)
                subdomains.append((subdomain, ip_address))
                print(f"Bulundu: {subdomain} - {ip_address}")
            except socket.gaierror:
                pass  
    return subdomains

def check_http_status(subdomains):
    for subdomain, ip in subdomains:
        try:
            url = f"http://{ip}"
            response = requests.get(url, timeout=3)
            print(f"Subdomain: {subdomain} - IP: {ip} - HTTP Yanıt Kodu: {response.status_code}")
        except requests.RequestException as e:
            print(f"Subdomain: {subdomain} - IP: {ip} - Hata: {str(e)}")

def main(domain, wordlist_file):
    subdomains = subdomain_brute_force(domain, wordlist_file)
    if subdomains:
        check_http_status(subdomains)
    else:
        print("Subdomain bulunamadı.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Subdomain brute force yapma ve IP adresi çözümleme.")
    parser.add_argument("-d", "--domain", required=True, help="Test etmek istediğiniz alan adı")
    parser.add_argument("-w", "--wordlist", required=True, help="Kullanmak istediğiniz wordlist dosyası")

    args = parser.parse_args()
    main(args.domain, args.wordlist)