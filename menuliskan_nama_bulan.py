print("Menuliskan Nama Bulan")

nomor = int(input("Nomor bulan: "))

bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni",
         "Juli", "Agustus", "September", "Oktober", "November", "Desember"]

if 1 <= nomor <= 12:
    print(bulan[nomor - 1])

else:
    print("Nomor bulan tidak valid")