print("Menghitung Upah Karyawan")

jam_kerja = int(input("Masukkan jam kerja: "))
upah_per_jam = 10000

if jam_kerja <= 12:
    print (f"Upah karyawan: {jam_kerja * upah_per_jam}")
else:
    lembur = jam_kerja - 12
    print (f"Upah karyawan: {(12 * upah_per_jam) + (lembur * upah_per_jam * 1.5)}")