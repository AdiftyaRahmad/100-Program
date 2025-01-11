def konversi_jarak(x):
    kilometer = x // 100000
    sisa_cm = x % 100000
    meter = sisa_cm // 100
    sisa_cm = sisa_cm % 100
    
    print(f"{kilometer} km + {meter} m + {sisa_cm} cm")

x = 261341
konversi_jarak(x)
