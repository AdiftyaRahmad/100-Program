
print("="*20)
print("Rumus Lingkaran")
print("="*20)

jari_jari = int(input("Jari-jari\t: "))

luas = lambda r : 3.14 * r * r
keliling = lambda r : 2 * 3.14 * r

print("Luas\t\t: ", luas(jari_jari))
print("Keliling\t: ", keliling(jari_jari))