print ("Program Selisih Waktu")

jam1 = int(input("Jam kesatu: "))
menit1 = int(input("Menit kesatu: "))
detik1 = int(input("Detik kesatu: "))

jam2 = int(input("Jam kedua: "))
menit2 = int(input("Menit kedua: "))
detik2 = int(input("Detik kedua: "))

total_detik1 = (jam1 * 3600) + (menit1 * 60) + detik1
total_detik2 = (jam2 * 3600) + (menit2 * 60) + detik2
selisih_detik = abs(total_detik1 - total_detik2)

jam_selisih = selisih_detik // 3600
sisa_detik_selisih = selisih_detik % 3600
menit_selisih = sisa_detik_selisih // 60
detik_selisih = sisa_detik_selisih % 60

print(f"Selisih Waktu: {jam_selisih} jam, {menit_selisih} menit, {detik_selisih} detik")