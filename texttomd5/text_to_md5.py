import hashlib

def md5_hash(text):
    hashed_text = hashlib.md5(text.encode()).hexdigest()
    return hashed_text

if __name__ == "__main__":
    clear_text = input("MD5 hash'e dönüştürülecek metni girin: ")
    hashed_text = md5_hash(clear_text)
    print("MD5 Hash değeri:", hashed_text)
