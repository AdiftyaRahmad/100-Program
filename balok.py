
print("="*20)
print("Rumus Balok")
print("="*20)

panjang = int(input("Panjang\t\t: "))
lebar = int(input("Lebar\t\t: "))
tinggi = int(input("Tinggi\t\t: "))

luas_permukaan = lambda p, l, t : 2 * (p * l + p * t + l * t)
volume = lambda p, l, t : p * l * t
keliling = lambda p, l, t : 4 * (p + l + t)

print(f"Luas Permukaan\t: {luas_permukaan(panjang, lebar, tinggi)}")
print(f"Volume\t\t: {volume(panjang, lebar, tinggi)}")
print(f"Keliling\t: {keliling(panjang, lebar, tinggi)}")