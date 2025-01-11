
print("="*20)
print("Rumus Segitiga")
print("="*20)

alas = int(input("Alas\t\t: "))
tinggi = int(input("Tinggi\t\t: "))
sisi1 = int(input("Sisi 1\t\t: "))
sisi2 = int(input("Sisi 2\t\t: "))
sisi3 = int(input("Sisi 3\t\t: "))

luas = lambda a, t : 1/2 * a * t
keliling = lambda s1, s2, s3 : s1 + s2 + s3

print("Keliling\t: ", keliling(sisi1, sisi2, sisi3))
print("Luas\t\t: ", luas(alas, tinggi))