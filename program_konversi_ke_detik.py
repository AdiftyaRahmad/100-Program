print ("Program Konversi ke Detik")

jam = int(input("Jam: "))
menit = int(input("Menit: "))
detik = int(input("Detik: "))

total_detik = (jam * 3600) + (menit * 60) + detik

print("Konversi ke Detik:", total_detik)