berat = float(input("masukkan berat badan anda : "))
tinggi = float(input("masukkan tinggi badan anda : "))
hasil = berat/((tinggi/100)**2)
if hasil < 18.5:
    print("berat badan anda kurang")
elif 18.5 <= hasil <= 22.9:
    print("berat badan anda normal")
elif 23 <= hasil <= 29.9:
    print("berat badan anda normal")
else :
    print("anda Obesitas")
