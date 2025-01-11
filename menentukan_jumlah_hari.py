print ("Menentukan Jumlah Hari")

bulan = int(input("Masukkan bulan: "))
tahun = int(input("Masukkan tahun: "))

if bulan in [1, 3, 5, 7, 8, 10, 12]:
    print (31)
elif bulan in [4, 6, 9, 11]:
    print (30)
elif bulan == 2:
    if tahun:
        print(29)
    else:
        print (28)
else:
    print("Bulan tidak valid")