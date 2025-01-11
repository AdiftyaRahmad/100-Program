def konversi_detik(total_detik):
    hari = total_detik // 86400
    sisa_detik = total_detik % 86400
    jam = sisa_detik // 3600
    sisa_detik %= 3600
    menit = sisa_detik // 60
    detik = sisa_detik % 60
    return hari, jam, menit, detik

total_detik = int(input("Masukkan durasi waktu dalam detik: "))

hari, jam, menit, detik = konversi_detik(total_detik)

print(f"{hari} hari, {jam} jam, {menit} menit, {detik} detik")

