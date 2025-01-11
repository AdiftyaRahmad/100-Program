
print("="*20)
print("Rumus Tabung")
print("="*20)

jari = int(input("Jari-jari\t: "))
tinggi = int(input("Tinggi\t\t: "))

luas_permukaan = lambda r, t : 2 * 3.14 * r * (r + t)
luas_selimut = lambda r, t : 2 * 3.14 * r * t
volume = lambda r, t : 3.14 * r * r * t

print(f"Luas Permukaan\t: {luas_permukaan(jari, tinggi)}")
print(f"Luas Selimut\t: {luas_selimut(jari, tinggi)}")
print(f"Volume\t\t: {volume(jari, tinggi)}")