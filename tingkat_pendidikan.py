import os
os.system("cls")

print("="*50)
print("Program Menentukan Tingkat Pendidikan Sesuai Umur")
print("="*50)

usia = int(input("Masukkan usia Anda\t: "))

print("="*50)

if usia < 5:
    print("Anda mungkin belum cukup umur untuk pendidikan formal.")
elif 5 <= usia <= 6:
    print("Anda berada di usia Taman Kanak-Kanak (TK).")
elif 7 <= usia <= 12:
    print("Anda berada di usia Sekolah Dasar (SD).")
elif 13 <= usia <= 15:
    print("Anda berada di usia Sekolah Menengah Pertama (SMP).")
elif 16 <= usia <= 18:
    print("Anda berada di usia Sekolah Menengah Atas (SMA).")
else:
    print("Anda mungkin berada di usia kuliah atau pendidikan lain.")

print("="*50)