def konversi_romawi(n):
    romawi_nilai = [
        (1000, "M"),
        (900, "CM"),
        (500, "D"),
        (400, "CD"),
        (100, "C"),
        (90, "XC"),
        (50, "L"),
        (40, "XL"),
        (10, "X"),
        (9, "IX"),
        (5, "V"),
        (4, "IV"),
        (1, "I")
    ]
    
    hasil = ""
    
    for nilai, simbol in romawi_nilai:
        while n >= nilai:
            hasil += simbol
            n -= nilai
    
    return hasil

n = int(input("Masukkan bilangan bulat positif: "))

print(f"Angka Romawi dari {n} adalah {konversi_romawi(n)}")
