import pyshark

def ag_trafigi_izle(interface):
    cap = pyshark.LiveCapture(interface=interface)
    for paket in cap.sniff_continuously(packet_count=10):
        print(paket)

interface = input("İzlenecek ağ arayüzünü girin: ")
ag_trafigi_izle(interface)
