def bulatkan_belanja(nilai_belanja):
    if nilai_belanja % 100 != 0:
        nilai_belanja -= nilai_belanja % 100
    elif nilai_belanja % 50 != 0:
        nilai_belanja -= nilai_belanja % 50
    elif nilai_belanja % 25 != 0:
        nilai_belanja -= nilai_belanja % 25
    return nilai_belanja

nilai_belanja = int(input("Masukkan total belanja: "))
nilai_belanja_bulat = bulatkan_belanja(nilai_belanja)

print(f"Nilai belanja yang dibulatkan ke pecahan terendah adalah: Rp{nilai_belanja_bulat}")

