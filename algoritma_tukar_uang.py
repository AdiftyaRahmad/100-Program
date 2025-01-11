def tukar_uang(uang):
    pecahan = [1000, 500, 100, 50, 25]
    for p in pecahan:
        jumlah_pecahan = uang // p
        uang = uang % p
        if jumlah_pecahan > 0:
            print(f"Jumlah pecahan Rp{p}: {jumlah_pecahan}")

uang = 2775
tukar_uang(uang)

