import os
os.system("cls")

print("="*50)
print("Menentukan Cuaca Berdasarkan Suhu Celcius")
print("="*50)

suhu = float(input("Masukkan Suhu Saat Ini (°C): "))

if suhu >= 30:
    print("Cuaca Panas.")
elif suhu >= 20:
    print("Cuaca Hangat.")
elif suhu >= 10:
    print("Cuaca Dingin.")
else:
    print("Cuaca Sangat Dingin.")

print("="*50)