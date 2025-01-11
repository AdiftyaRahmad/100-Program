gaji_per_jam = 10000
total_gaji_perusahaan = 0

n = int(input("Jumlah karyawan: "))

for i in range(n):
    print(f"Karyawan {i+1}")
    jam_kerja = int(input("Jam kerja karyawan: "))
    
    if jam_kerja > 7:
        jam_lembur = jam_kerja - 7
        gaji_reguler = 7 * gaji_per_jam
        gaji_lembur = jam_lembur * gaji_per_jam * 1.5
        total_gaji = gaji_reguler + gaji_lembur
    else:
        total_gaji = jam_kerja * gaji_per_jam
    
    total_gaji_perusahaan += total_gaji
    print(f"Total gaji: {total_gaji}")

print(f"Total gaji karyawan: {total_gaji_perusahaan}")