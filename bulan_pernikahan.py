bulan_saat_ini = int(input("Bulan saat ini: "))
bulan_kedepan = int(input("Bulan kedepan: "))

total_bulan = bulan_saat_ini + bulan_kedepan
bulan_pernikahan = total_bulan % 12

if bulan_pernikahan == 0:
    bulan_pernikahan = 12

print(f"Bulan pernikahan: {bulan_pernikahan}")