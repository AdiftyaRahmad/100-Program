def cek_berat_badan_ideal(BB, TB):
    BB_ideal = TB - 100
    selisih = abs(BB - BB_ideal)
    
    if selisih <= 2:
        return "ideal"
    else:
        return "tidak ideal"

BB = float(input("Masukkan berat badan (kg): "))
TB = float(input("Masukkan tinggi badan (cm): "))

hasil = cek_berat_badan_ideal(BB, TB)
print("Status berat badan: ", hasil)

