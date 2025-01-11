import os
os.system("cls")

print("="*30)
bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni",
         "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
bulan[7] = "August"
bulan[0] = "January"

bulan.append("Muharram")

for i, data in enumerate(bulan):
    print(f"Bulan ke-{i+1} : {data}")
print("="*30)