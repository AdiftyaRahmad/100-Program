char = input("Masukkan karakter: ")

if char.isdigit():
    nilai_integer = ord(char) - ord('0')
else:
    nilai_integer = -99

print("Nilai integer:", nilai_integer)

