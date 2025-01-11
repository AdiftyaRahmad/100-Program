print("Menentukan Jam Berikutnya")

jam = int(input("Masukkan jam: "))
menit = int(input("Masukkan menit: "))
detik = int(input("Masukkan detik: "))

detik += 1

if detik == 60:

    detik = 0
    menit += 1
    if menit == 60:
        menit = 0
        jam += 1
        if jam == 24:
            jam = 0

print (f"{jam:02}:{menit:02}:{detik:02}")