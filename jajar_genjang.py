
print("="*20)
print("Rumus Jajar Genjang")
print("="*20)

alas = int(input("Alas\t\t: "))
tinggi = int(input("Tinggi\t\t: "))
sisi_miring = int(input("Sisi Miring\t: "))

luas = lambda a, t : a * t
keliling = lambda a, sm : 2 * (a + sm)

print("Luas\t\t: ", luas(alas, tinggi))
print("Keliling\t: ", keliling(alas, sisi_miring))   