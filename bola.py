
print("="*20)
print("Rumus Bola")
print("="*20)

jari = int(input("Jari-jari\t: "))

luas = lambda r :  4 * 3.14 * r * r
volume = lambda r : 4/3 * 3.14 * r * r * r

print(f"Luas\t\t: {round(luas(jari), 2)}")
print(f"Volume\t\t: {round(volume(jari), 2)}")