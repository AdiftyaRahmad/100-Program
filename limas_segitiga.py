
print("="*20)
print("Rumus Limas Segitiga")
print("="*20)

alas = int(input("Alas\t: "))
tinggi_segitiga = int(input("Tinggi Segitiga\t: "))
tinggi_limas = int(input("Tinggi Limas\t: "))
sisi1 = int(input("Sisi 1\t: "))
sisi2 = int(input("Sisi 2\t: "))
sisi3 = int(input("Sisi 3\t: "))

luas_alas = lambda a, t: 1/2 * a * t
luas_sisi1 = lambda a, t: 1/2 * a * t
luas_sisi2 = lambda a, t: 1/2 * a * t
luas_sisi3 = lambda a, t: 1/2 * a * t

luas_permukaan = lambda a, s1, s2, s3, t: luas_alas(a, t) + luas_sisi1(a, s1) + luas_sisi2(a, s2) + luas_sisi3(a, s3)
volume = lambda a, t1, t2: 1/3 * luas_alas(a, t1) * t2

print(f"Luas Permukaan\t: {luas_permukaan(alas, sisi1, sisi2, sisi3, tinggi_segitiga)}")
print(f"Volume\t\t: {round(volume(alas, tinggi_segitiga, tinggi_limas), 2)}")
