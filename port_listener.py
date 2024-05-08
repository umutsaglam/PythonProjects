import socket

def main():
    HOST = '0.0.0.0' 
    PORT = int(input("Dinlemek istediğiniz port numarasını girin: "))  

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print(f"Dinleniyor: {HOST}:{PORT}")

        while True:
            conn, addr = s.accept()
            with conn:
                print('Bağlantı geldi:', addr)
                data = conn.recv(1024)
                print('Gelen veri:', data.decode())

if __name__ == "__main__":
    main()
