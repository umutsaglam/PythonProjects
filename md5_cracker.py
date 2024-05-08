import hashlib

def crack_hash(hashed_password, wordlist):
    with open(wordlist, 'r', encoding='latin-1') as f:
        for line in f:
            password = line.strip()
            if hashlib.md5(password.encode()).hexdigest() == hashed_password:
                return password
    return "Hash kırılamadı."

if __name__ == "__main__":
    hashed_password = input("Kırılacak hash değeri: ")
    wordlist = input("Wordlist dosyası: ")
    cracked_password = crack_hash(hashed_password, wordlist)
    print("Kırılan parola:", cracked_password)
