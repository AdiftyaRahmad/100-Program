import os
os.system("cls")

print("="*30)
print("Menentukan Bilangan")

def cek_bilangan(angka):
    if angka > 0:
        return "Positif"
    elif angka < 0:
        return "Negatif"
    return "Nol"

print("="*30)
angka = int(input("Inputkan Angka: "))
print(f"{angka} adalah bilangan {cek_bilangan(angka)}.")
print("="*30)