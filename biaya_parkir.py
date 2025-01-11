jam_masuk = int(input("Jam masuk: "))
jam_keluar = int(input("Jam keluar: "))

if jam_keluar < jam_masuk:
    print("Jam keluar tidak boleh lebih awal dari jam masuk.")
else:
    lama_parkir = jam_keluar - jam_masuk
    biaya = 2000

if lama_parkir > 2:
    biaya += (lama_parkir - 2) * 500

print (f"Biaya = {biaya}")