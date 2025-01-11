print("Pencarian dari Suatu Array")

array = [3, 5, 7, 9, 11, 13, 15]
target = int(input("Pilih (1-15): "))
ditemukan = False

for i in range (len(array)):
    if array [i] == target:
        print(f"Elemen {target} di temukan di index {i}")
        ditemukan = True
        break

if not ditemukan:
    print(f"Elemen {target} tidak ditemukan")