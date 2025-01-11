def cek_jenis_segitiga(a, b, c):
    if a > b:
        a, b = b, a
    if b > c:
        b, c = c, b
    if a > b:
        a, b = b, a
    
    if a**2 + b**2 == c**2:
        return "Segitiga Siku-siku"
    elif a**2 + b**2 > c**2:
        return "Segitiga Lancip"
    else:
        return "Segitiga Tumpul"

a = int(input("Masukkan sisi a: "))
b = int(input("Masukkan sisi b: "))
c = int(input("Masukkan sisi c: "))

print(cek_jenis_segitiga(a, b, c))

