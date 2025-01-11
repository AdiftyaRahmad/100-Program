def konversi_panjang(panjang_dalam_meter):
    konversi_inci = panjang_dalam_meter * (1000 / 25.4)
    konversi_kaki = panjang_dalam_meter * (100 / 30.48)
    konversi_yard = panjang_dalam_meter / 0.9144
    
    print(f"Panjang dalam inci: {konversi_inci} inci")
    print(f"Panjang dalam kaki: {konversi_kaki} kaki")
    print(f"Panjang dalam yard: {konversi_yard} yard")

panjang_meter = float(input("Masukkan panjang benda dalam meter: "))
konversi_panjang(panjang_meter)

