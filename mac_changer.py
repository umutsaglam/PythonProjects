import subprocess

def change_mac(interface, new_mac):
    print("[+] MAC adresi değiştiriliyor...")
    subprocess.call(["sudo", "ifconfig", interface, "down"])
    subprocess.call(["sudo", "ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["sudo", "ifconfig", interface, "up"])
    print("[+] MAC adresi değiştirildi!")

interface = input("MAC adresini değiştirmek istediğiniz ağ arayüzünü girin: ")
new_mac = input("Yeni MAC adresini girin: ")

change_mac(interface, new_mac)
