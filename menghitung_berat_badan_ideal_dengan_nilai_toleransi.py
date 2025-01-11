print("Menghitung Berat Badan Ideal dengan Nilai Toleransi")

tinggi = int(input("Masukkan tinggi badan: "))
toleransi = 5

ideal = tinggi - 100
batas_bawah = ideal - toleransi
batas_atas = ideal + toleransi

print (f"Berat badan ideal adalah antara {batas_bawah}kg hingga {batas_atas}kg")