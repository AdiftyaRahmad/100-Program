print ("Konversi Suhu (C, F, K, R)")

celsius = float(input("Masukkan Celcius: "))

fahrenheit = (celsius * 9/5) + 32
print(f"{celsius} C ke Fahrenheit:", fahrenheit)

kelvin = celsius + 273.15
print(f"{celsius} C ke Kelvin:", kelvin)

reamur = celsius * 4/5
print(f"{celsius} C ke Reamur:", reamur)