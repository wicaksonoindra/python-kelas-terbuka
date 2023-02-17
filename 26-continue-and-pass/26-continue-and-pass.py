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
angka = 0
print(f"angka sekarang -> {angka}")

while angka < 5:
    angka+=1
    print(f"angka sekarang -> {angka}") # aksi 1
    if angka == 3:
        print("nice!")
        continue # akan membuat loop meloncat ke step selanjutnya
    print("whassup!") # aksi ke 2

print("Nice!")
