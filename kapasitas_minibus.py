jumlah_peserta = int(input("Jumlah peserta: "))

kapasitas_minibus = 7
jumlah_minibus = jumlah_peserta // kapasitas_minibus

if jumlah_peserta % kapasitas_minibus != 0:
    jumlah_minibus += 1

print (f"Jumlah minibus: {jumlah_minibus}")