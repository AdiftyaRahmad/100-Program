def hitung_volume(m):
    V = (4/3) * (m ** 3)
    return V

massa = float(input("Masukkan nilai massa (m): "))
volume = hitung_volume(massa)
print(f"Volume V untuk massa {massa} adalah {volume}")

