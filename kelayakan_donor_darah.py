import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

clear_screen()

print("-"*30)
print("Cek Kelayakan Donor Darah")
print("-"*30)

try:
    usia = int(input("Usia anda: "))
    bb = int(input("Berat badan anda: "))
    kondisi = input("Kondisi anda (Sehat/Tidak): ")

    if usia >= 18 and usia <= 60 and bb >= 50 and kondisi.lower() == "sehat":
        print(f"Usia: {usia}\nBerat badan: {bb}\nKondisi: {kondisi}\nAnda layak menjadi pendonor darah.")
    else:
        print(f"Usia: {usia}\nBerat badan: {bb}\nKondisi: {kondisi}\nAnda belum layak menjadi pendonor darah.")
except ValueError:
    print("Input tidak valid. Harap masukkan angka yang benar.")