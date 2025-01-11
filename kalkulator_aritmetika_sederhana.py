operand1 = float(input("Masukkan operand 1: "))
operator = input("Masukkan operator (+, -, *, /): ")
operand2 = float(input("Masukkan operand 2: "))

if operator == '+':
    hasil = operand1 + operand2
elif operator == '-':
    hasil = operand1 - operand2
elif operator == '*':
    hasil = operand1 * operand2
elif operator == '/':
    if operand2 != 0:
        hasil = operand1 / operand2
    else:
        hasil = "Tidak dapat dibagi dengan nol"
else:
    hasil = "Operator tidak valid"

print(f"Hasil dari {operand1} {operator} {operand2} = {hasil}")

