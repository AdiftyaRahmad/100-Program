print ("Menentukan Huruf Vokal atau Konsonan")

huruf = input ("Masukkan huruf: ")
vokal = "aiueo"

if huruf.lower() in vokal:
    print (f"{huruf} adalah huruf vokal")
else:
    print (f"{huruf} adalah huruf konsonan")