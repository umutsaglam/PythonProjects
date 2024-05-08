import base64

def base64_encode(text):
    return base64.b64encode(text.encode()).decode()

def base64_decode(text):
    return base64.b64decode(text.encode()).decode()

def hex_encode(text):
    return text.encode().hex()

def hex_decode(text):
    return bytes.fromhex(text).decode()

def binary_encode(text):
    return ' '.join(format(ord(char), '08b') for char in text)

def binary_decode(text):
    binary_values = text.split()
    return ''.join(chr(int(b, 2)) for b in binary_values)

def reverse_text(text):
    return text[::-1]

def main():
    choice = input("Encode için 'e', Decode için 'd' yazın: ")

    if choice == 'e':
        text = input("Şifrelenecek metni girin: ")
        encode_choice = input("Base64 için 'b', Hexadecimal için 'h', Binary için 'n' girin: ")

        if encode_choice == 'b':
            encoded_text = base64_encode(text)
        elif encode_choice == 'h':
            encoded_text = hex_encode(text)
        elif encode_choice == 'n':
            encoded_text = binary_encode(text)
        else:
            print("Geçersiz seçenek!")
            return

        print("Şifreli metin:", encoded_text)

    elif choice == 'd':
        text = input("Çözülecek metni girin: ")
        decode_choice = input("Base64 için 'b', Hexadecimal için 'h', Binary için 'n' girin: ")

        if decode_choice == 'b':
            decoded_text = base64_decode(text)
        elif decode_choice == 'h':
            decoded_text = hex_decode(text)
        elif decode_choice == 'n':
            decoded_text = binary_decode(text)
        else:
            print("Geçersiz seçenek!")
            return

        print("Çözülmüş metin:", decoded_text)

    else:
        print("Geçersiz seçenek!")

if __name__ == "__main__":
    main()
