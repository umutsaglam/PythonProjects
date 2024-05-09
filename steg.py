from PIL import Image

def gizle(fotograf_yolu, gizlenecek_dosya_yolu, hedef_yol):
    with Image.open(fotograf_yolu) as img:
        img = img.convert('RGB')
        gizlenecek_veri = bytearray(open(gizlenecek_dosya_yolu, 'rb').read())
        gizlenecek_veri += bytes([0] * (len(gizlenecek_veri) % 3))
        gizlenecek_veri += b'\x00' * (3 - len(gizlenecek_veri) % 3)
        
        veri_index = 0
        for x in range(img.width):
            for y in range(img.height):
                r, g, b = img.getpixel((x, y))
                if veri_index < len(gizlenecek_veri):
                    r = (r & 0b11111110) | ((gizlenecek_veri[veri_index] & 0b10000000) >> 7)
                    g = (g & 0b11111110) | ((gizlenecek_veri[veri_index] & 0b01000000) >> 6)
                    b = (b & 0b11111100) | ((gizlenecek_veri[veri_index] & 0b00111111) >> 0)
                    veri_index += 1
                img.putpixel((x, y), (r, g, b))
        
        img.save(hedef_yol)

def cikar(gizli_fotograf_yolu):
    with Image.open(gizli_fotograf_yolu) as img:
        img = img.convert('RGB')
        
        gizlenecek_veri = bytearray()
        for x in range(img.width):
            for y in range(img.height):
                r, g, b = img.getpixel((x, y))
                gizlenecek_veri.append(((r & 1) << 7) | ((g & 1) << 6) | ((b & 3) << 0))
        
        dosya_adı = gizli_fotograf_yolu.split('.')[0] + "_cikarilan." + gizli_fotograf_yolu.split('.')[1]
        with open(dosya_adı, 'wb') as dosya:
            dosya.write(gizlenecek_veri)

if __name__ == "__main__":
    fotograf_yolu = input("Fotoğraf yolunu girin: ")
    secim = input("1: Gizle\n2: Çıkar\nSeçiminizi yapın (1 veya 2): ")

    if secim == '1':
        gizlenecek_dosya_yolu = input("Gizlenecek dosya yolunu girin: ")
        hedef_yol = input("Hedef fotoğraf yolunu girin: ")
        gizle(fotograf_yolu, gizlenecek_dosya_yolu, hedef_yol)
        print("Dosya başarıyla gizlendi.")
    elif secim == '2':
        cikar(fotograf_yolu)
        print("Dosya başarıyla çıkarıldı.")
    else:
        print("Geçersiz seçim.")
