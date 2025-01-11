print ("Rumus Geometri (Luas Persegi, Lingkaran, Segitiga)")

sisi = float(input("Sisi: "))
luas_persegi = sisi * sisi
print("Luas Persegi:", luas_persegi)

radius = float(input("Radius: "))
luas_lingkaran = 3.14 * radius ** 2
print("Luas Lingkaran:", luas_lingkaran)

alas = float(input("Alas: "))
tinggi = float(input("Tinggi: "))
luas_segitiga = 0.5 * alas * tinggi
print("Luas Segitiga:", luas_segitiga)