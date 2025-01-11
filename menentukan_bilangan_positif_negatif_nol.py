print("Menentukan Bilangan Positif/Negatif/Nol")

bilangan = float(input("Masukkan bilangan: "))

if bilangan > 0:
    print(f"{bilangan} adalah bilangan positif")
elif bilangan < 0:
    print(f"{bilangan} adalah bilangan negatif")
else:
    print(f"{bilangan} adalah nol")