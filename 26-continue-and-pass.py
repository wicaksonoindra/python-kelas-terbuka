# Control Flow: Continue, pass, break

# Pass -> berfungsi sebagai dummy, tidak akan di eksekusi

angka = 0

while angka < 5:
    angka += 1
    if angka == 3:
        pass # tidak akan di eksekusi
        print("whadaaap!")
    print(angka)

# Continue
