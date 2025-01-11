print ("Mencari Bilangan Terbesar dan Terkecil dari 3 Angka")

x = int(input("Bilangan 1: "))
y = int(input("Bilangan 2: "))
z = int(input("Bilangan 3: "))

terbesar = max(x, y, z)
terkecil = min(x, y, z)

print(f"Bilangan terbesar adalah {terbesar}")
print(f"Bilangan terkecil adalah {terkecil}")