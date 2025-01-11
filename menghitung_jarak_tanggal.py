def hitung_selisih_tanggal(tanggal1, tanggal2):
    def konversi_ke_hari(dd, mm, yy):
        return (yy * 365) + (mm * 30) + dd

    dd1, mm1, yy1 = tanggal1
    dd2, mm2, yy2 = tanggal2

    total_hari1 = konversi_ke_hari(dd1, mm1, yy1)
    total_hari2 = konversi_ke_hari(dd2, mm2, yy2)

    selisih_hari = abs(total_hari2 - total_hari1)

    tahun = selisih_hari // 365
    sisa_hari = selisih_hari % 365
    bulan = sisa_hari // 30
    hari = sisa_hari % 30

    return tahun, bulan, hari

tanggal1 = (1, 1, 2000)
tanggal2 = (15, 3, 2002)

tahun, bulan, hari = hitung_selisih_tanggal(tanggal1, tanggal2)

print(f"Selisih: {tahun} tahun, {bulan} bulan, {hari} hari")

