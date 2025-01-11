print("Pembulatan ke Mata Uang Terkecil")

nilai = int(input("Masukkan nilai: "))
kelipatan = int(input("Masukkan kelipatan: "))

pembulatan = round (nilai / kelipatan) * kelipatan

print (pembulatan)