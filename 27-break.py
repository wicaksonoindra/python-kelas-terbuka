# Break
# Contoh 1
angka = 0

while angka < 5:
    angka += 1
    print(f"angka sekarang -> {angka}")

    if angka == 3:
        print("Nice!")
        break

    print("whassup!")

print("Cukup Finish!")

# Contoh 2
data_int = int(input("Hitung sampai = "))

angka = 0

while True:
    angka += 1
    print(f"angka sekarang -> {angka}")

    if angka == data_int:
        print("Nice!")
        break

    print("whassup!")

print("Cukup Finish!")
