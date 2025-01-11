import os
os.system("cls")

print("Menghitung Diskon Berdasarkan Total Belanja")
def hitung_diskon(total_belanja):
    if total_belanja >= 50000:
        return total_belanja * 0.5
    return 0

print("="*30)
total_belanja = int(input("Total Belanja Anda: "))
diskon = hitung_diskon(total_belanja)
total_bayar = total_belanja - diskon
print(f"Total yang harus dibayar: Rp.{total_bayar}")
print("="*30)