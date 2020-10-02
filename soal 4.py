N = int(input("berapa angka = "))
ruang = []
for i in range(N):
    ruang.append(int(input("masukkan angka ke {} = ".format(i))))
print("Nilai Maksimal = {}".format(max(ruang)))
print("Nilai Minimum = {}".format(min(ruang)))
