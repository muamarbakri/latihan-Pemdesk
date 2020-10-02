username = "muamar"
password = 190411100060
i=1
while True:
    getUsername = input("masukkan username = ")
    if getUsername == username:
        break
    else:
        print("username salah")
while i <= 3:
    getPassword = int(input("masukkan password = "))
    if getPassword == password:
        print("Anda berhasil login")
        break
    else:
        print("password salah")
    if i == 3:
        print("maaf user name dan password salah")
        break
    i+= 1
