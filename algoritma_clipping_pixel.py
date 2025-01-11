def clipping(value):
    if value > 255:
        return 255
    elif value < 0:
        return 0
    else:
        return value

input_values = [260, -10, 120, 300, 255, -5]
clipped_values = [clipping(value) for value in input_values]

print("Nilai sebelum clipping:", input_values)
print("Nilai setelah clipping:", clipped_values)

