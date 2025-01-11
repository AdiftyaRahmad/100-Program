def jumlah_hari(bulan, tahun):
    hari_per_bulan = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    if (tahun % 4 == 0 and tahun % 100 != 0) or (tahun % 400 == 0):
        hari_per_bulan[1] = 29
    
    return hari_per_bulan[bulan - 1]

bulan = int(input("Masukkan nomor bulan (1-12): "))
tahun = int(input("Masukkan tahun: "))

jumlah = jumlah_hari(bulan, tahun)
print(f"Jumlah hari di bulan {bulan} tahun {tahun} adalah {jumlah} hari.")

