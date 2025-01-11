golongan = int(input("Golongan: "))
pemakaian_kwh = int(input("Pemakaian: "))

if golongan == 1:
    tarif = 1000
elif golongan == 2:
    tarif = 2000

if pemakaian_kwh < 100:
    pemakaian_kwh = 100

total_tagihan = pemakaian_kwh * tarif

if pemakaian_kwh >= 1000:
    total_tagihan += total_tagihan * 0.10

print(f"Bayar: {total_tagihan}")