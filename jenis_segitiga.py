import os
os.system("cls")

print("="*30)
print("Menentukan Jenis Segitiga")
print("="*30)

a = float(input("Masukkan Sisi Pertama: "))
b = float(input("Masukkan Sisi Kedua: "))
c = float(input("Masukkan Sisi Ketiga: "))

if a == b == c:
    print("Segitiga Sama Sisi.")
elif a == b or b == c or a == c:
    print("Segitiga Sama Kaki.")
else:
    print("Segitiga Sembarang.")

print("="*30)