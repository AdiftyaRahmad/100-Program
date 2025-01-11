import os
os.system("cls")

print("="*30)
print("Cek Kecocokan Berat Badan")
print("="*30)

berat = float(input("Masukkan berat badan (kg): "))
tinggi = float(input("Masukkan tinggi badan (m): "))

print("="*30)

bmi = berat / (tinggi ** 2)

if bmi < 18.5:
    print("Berat Badan Kamu Kurang.")
elif bmi < 24.9:
    print("Berat Badan Kamu Normal.")
elif bmi < 29.9:
    print("kamu Kelebihan Berat Badan.")
else:
    print("kamu Mengalami Obesitas.")

print("="*30)