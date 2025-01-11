print ("Program Konversi Detik ke Jam, Menit, Detik")

total_detik = int(input("Masukkan Detik: "))

jam = total_detik // 3600
sisa_detik = total_detik % 3600
menit = sisa_detik // 60
detik = sisa_detik % 60

print(f"{total_detik} Detik = {jam} jam, {menit} menit, {detik} detik")