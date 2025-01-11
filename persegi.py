
print("="*20)
print("Rumus Persegi")
print("="*20)

sisi = int(input("Sisi\t\t: "))
luas = lambda s : s * s
keliling = lambda x : 4 * x

print("Luas\t\t: ", luas(sisi))
print("Keliling\t: ", keliling(sisi))