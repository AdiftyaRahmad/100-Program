print ("Program Gaji Bersih Karyawan")

gaji_kotor = float(input("Gaji Kotor: "))
pajak = float(input("Pajak: "))
asuransi = float(input("Asuransi: "))

gaji_bersih = gaji_kotor - (gaji_kotor * pajak) - asuransi

print("Gaji Bersih Karyawan:", gaji_bersih)