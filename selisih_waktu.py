jam_mulai = int(input("Masukkan jam mulai: "))
menit_mulai = int(input("Masukkan menit mulai: "))

jam_selesai = int(input("Masukkan jam selesai: "))
menit_selesai = int(input("Masukkan menit selesai: "))

total_menit_mulai = jam_mulai * 60 + menit_mulai
total_menit_selesai = jam_selesai * 60 + menit_selesai

selisih_menit = total_menit_selesai - total_menit_mulai

if selisih_menit < 0:
    selisih_menit += 24 * 60 

selisih_jam = selisih_menit // 60
sisa_menit = selisih_menit % 60

print(f"Selisih waktu adalah {selisih_jam} jam {sisa_menit} menit.")