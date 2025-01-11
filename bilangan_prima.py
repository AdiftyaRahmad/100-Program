import os

os.system("cls" if os.name == "nt" else "clear")

def is_prime(angka):
    if angka > 1:
        for i in range(2, angka):
            if (angka % i) == 0:
                return False
        return True
    return False

print("="*20)
print("Cek Bilangan Prima")
print("="*20)

try:
    angka = int(input("Inputkan angka: "))
    if is_prime(angka):
        print(f"Angka {angka} ialah bilangan prima.")
    else:
        print(f"Angka {angka} bukan bilangan prima.")
except ValueError:
    print("Input tidak valid. Harap masukkan angka bulat.")