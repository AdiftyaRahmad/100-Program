def nama_bulan(bulan):
    bulan_dict = {
        1: "Januari",
        2: "Februari",
        3: "Maret",
        4: "April",
        5: "Mei",
        6: "Juni",
        7: "Juli",
        8: "Agustus",
        9: "September",
        10: "Oktober",
        11: "November",
        12: "Desember"
    }
    
    if 1 <= bulan <= 12:
        return bulan_dict[bulan]
    else:
        return "Nomor bulan tidak valid"

nomor_bulan = int(input("Masukkan nomor bulan (1-12): "))
print(nama_bulan(nomor_bulan))

