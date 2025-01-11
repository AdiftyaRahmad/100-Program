def hitung_berat_ideal(tinggi_badan):
    hasil_pertama = tinggi_badan - 100
    sepuluh_persen = hasil_pertama * 0.10
    berat_ideal = hasil_pertama - sepuluh_persen
    return berat_ideal

tinggi_badan = float(input("Masukkan tinggi badan (dalam cm): "))
berat_ideal = hitung_berat_ideal(tinggi_badan)
print(f"Berat badan ideal untuk tinggi {tinggi_badan} cm adalah {berat_ideal:.2f} kg.")

