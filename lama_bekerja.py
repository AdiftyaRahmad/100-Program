jam_masuk = int(input("Jam masuk (1-12): "))
jam_keluar = int(input("Jam keluar (1-12): "))

if jam_masuk > jam_keluar:
    lama_kerja = (12 - jam_masuk) + jam_keluar
else:
    lama_kerja = jam_keluar - jam_masuk

print (f"Lama bekerja: {lama_kerja} jam.")