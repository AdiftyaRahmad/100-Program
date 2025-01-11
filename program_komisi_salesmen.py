print ("Program Komisi Salesman")

penjualan = float(input("Masukkan Total Penjualan: "))
if penjualan > 100000:
    komisi = penjualan * 0.1
else:
    komisi = penjualan * 0.05
print("Komisi Salesman:", komisi)