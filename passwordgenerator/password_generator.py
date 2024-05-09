import random


def sifreUret(sifreUzunlugu):
    alfabe = "abcdefghijklmnopqrstuvwxyz"

    sifreler = []

    for uzunluk in sifreUzunlugu:

        sifre = ""
        for j in range(uzunluk):
            sonraki_harf_indeks = random.randrange(len(alfabe))
            sifre = sifre + alfabe[sonraki_harf_indeks]

        sifre = rakamlaDegistir(sifre)
        sifre = buyukHarfleDegistir(sifre)

        sifreler.append(sifre)

    return sifreler


def rakamlaDegistir(sifre):
    for i in range(random.randrange(1, 3)):
        degistir_indeks = random.randrange(len(sifre) // 2)
        sifre = sifre[0:degistir_indeks] + str(random.randrange(10)) + sifre[degistir_indeks + 1:]
        return sifre


def buyukHarfleDegistir(sifre):
    for i in range(random.randrange(1, 3)):
        degistir_indeks = random.randrange(len(sifre) // 2, len(sifre))
        sifre = sifre[0:degistir_indeks] + sifre[degistir_indeks].upper() + sifre[degistir_indeks + 1:]
        return sifre


def main():
    sifreSayisi = int(input("Kaç adet şifre üretmek istiyorsunuz? "))

    print(str(sifreSayisi) + " şifre üretiliyor")

    sifreUzunluklari = []

    print("Şifrenin minimum uzunluğu 3 olmalıdır.")

    for i in range(sifreSayisi):
        uzunluk = int(input("Şifre #" + str(i + 1) + " için uzunluğu girin: "))
        if uzunluk < 3:
            uzunluk = 3
        sifreUzunluklari.append(uzunluk)

    Sifre = sifreUret(sifreUzunluklari)

    for i in range(sifreSayisi):
        print("Şifre #" + str(i + 1) + " = " + Sifre[i])


main()
