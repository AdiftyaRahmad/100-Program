import os
os.system("cls")

print("="*40)
print("Menghitung Tarif Parkir Per-jam")
print("="*40)

jam_parkir = int(input("Berapa Jam Anda Parkir?: "))

print("="*40)

if jam_parkir <= 1:
    tarif = 5000
else:
    tarif = 5000 + (jam_parkir - 1) * 3000

print(f"Tarif Parkir Yang Harus Dibayar: Rp {tarif}")

print("="*40)