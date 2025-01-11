import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

clear_screen()

print("-"*20)
print("Cek Kategori Usia")
print("-"*20)

try:
    usia = int(input("Inputkan usia anda: "))
    if usia < 13:
        print(f"Usia {usia}:\nKategori anak-anak.")
    elif usia < 18:
        print(f"Usia {usia}:\nKategori remaja.")
    elif usia < 60:
        print(f"Usia {usia}:\nKategori dewasa.")
    else:
        print(f"Usia {usia}:\nKategori lansia.")
except ValueError:
    print("Input tidak valid. Harap masukkan angka.")
