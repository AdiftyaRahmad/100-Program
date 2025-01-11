def tentukan_indeks(nilai_ujian):
    if nilai_ujian >= 80:
        indeks_nilai = 'A'
    elif nilai_ujian >= 70:
        indeks_nilai = 'B'
    elif nilai_ujian >= 55:
        indeks_nilai = 'C'
    elif nilai_ujian >= 40:
        indeks_nilai = 'D'
    else:
        indeks_nilai = 'E'
    
    print(f"Nilai ujian: {nilai_ujian}")
    print(f"Indeks nilai: {indeks_nilai}")

nilai_ujian = int(input("Masukkan nilai ujian: "))
tentukan_indeks(nilai_ujian)
