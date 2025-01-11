def hitung_upah(golongan, jam_kerja, jam_lembur=0):
    if golongan in ['a', 'b', 'c', 'd']:
        upah_per_jam = 4000
    else:
        raise ValueError("Golongan tidak valid")

    upah_kerja = jam_kerja * upah_per_jam
    upah_lembur = 0
    if jam_lembur > 0:
        upah_lembur = jam_lembur * upah_per_jam * 1.5

    upah_total = upah_kerja + upah_lembur
    return upah_total

golongan = 'c'
jam_kerja = 40
jam_lembur = 10

upah_total = hitung_upah(golongan, jam_kerja, jam_lembur)
print(f"Upah total untuk golongan {golongan}, {jam_kerja} jam kerja dan {jam_lembur} jam lembur: Rp {upah_total}")

