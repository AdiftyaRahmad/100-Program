
print("="*20)
print("Rumus Kerucut")
print("="*20)

jari = int(input("Jari-jari\t: "))
garis_pelukis = int(input("Garis Pelukis\t: "))
tinggi = int(input("Tinggi\t\t: "))

luas_permukaan = lambda r, s : 3.14 * r * (r + s)
luas_selimut = lambda r, s : 3.14 * r * s
volume = lambda r, t : 1/3 * 3.13 * r * r * t

print(f"Luas Permukaan\t: {luas_permukaan(jari, garis_pelukis)}")
print(f"Luas Selimut\t: {luas_selimut(jari, garis_pelukis)}")
print(f"Volume\t\t: {round(volume(jari, tinggi), 2)}")