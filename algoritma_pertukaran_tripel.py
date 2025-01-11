x = int(input("Masukkan nilai x: "))
y = int(input("Masukkan nilai y: "))
z = int(input("Masukkan nilai z: "))

temp = x
x = y
y = z
z = temp

print(f"Nilai setelah pertukaran: x = {x}, y = {y}, z = {z}")

