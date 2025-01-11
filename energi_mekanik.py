import os
os.system("cls")

print("="*20)
print("Energi Mekanik")
print("="*20)

m = int(input("Masukkan massa: "))
h = int(input("Masukkan ketinggian: "))
v = int(input("Masukkan kecepatan benda: "))
g = 10

ep = m * g * h
ek = 1/2 * m * v * v
em = ep + ek

print(f"Energi Potensial: {ep}")
print(f"Energi Kinetik: {ek}")
print(f"Energi Mekanik: {em}")