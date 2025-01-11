
print("="*20)
print("Rumus Trapesium")
print("="*20)

sisi1 = int(input("Sisi Sejajar 1\t\t: "))
sisi2 = int(input("Sisi Sejajar 2\t\t: "))
sisi3 = int(input("Sisi Tidak Sejajar 1\t: "))
sisi4 = int(input("Sisi Tidak Sejajar 2\t: "))
tinggi = int(input("Tinggi\t\t\t: "))

luas = lambda s1, s2, t : 1/2 * (s1 + s2) * t
keliling = lambda s1, s2, s3, s4 : s1 + s2 + s3 + s4

print("Luas\t\t\t: ", luas(sisi1, sisi2, tinggi))
print("Keliling\t\t: ", keliling(sisi1, sisi2, sisi3, sisi4))