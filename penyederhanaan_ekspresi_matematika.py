def calculate_x(b, c, a):
    x = (-b + 2*c**2 + 4*a*b) / (2*c)
    return x
b = 5
c = 3
a = 2
result = calculate_x(b, c, a)
print(f"Nilai x adalah: {result}")
