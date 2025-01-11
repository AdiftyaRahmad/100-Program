x = int(input("Masukkan jumlah hari: "))

tahun = x // 365
sisa_hari = x % 365
bulan = sisa_hari // 30
hari = sisa_hari % 30

print(f"Jumlah waktu: {tahun} tahun, {bulan} bulan, {hari} hari")

