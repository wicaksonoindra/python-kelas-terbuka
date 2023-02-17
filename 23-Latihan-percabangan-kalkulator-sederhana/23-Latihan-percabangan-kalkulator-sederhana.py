# Latihan
# Kalkulator sederhana
print("\n"+20*"=")
print("Kalkulator Sederhana")
print(20*"=")
angka_1 = float(input("Masukkan angka 1= "))
operator = input("Masukkan operator(+,-,x,/): ")
angka_2 = float(input("Masukkan angka 2= "))

if operator == "+":
    hasil = angka_1 + angka_2
    print(f"Hasil dari {angka_1} + {angka_2} adalah {hasil}")
elif operator == "-":
    hasil = angka_1 - angka_2
    print(f"Hasil dari {angka_1} - {angka_2} adalah {hasil}")
elif operator == "x" or operator == "*":
    hasil = angka_1 * angka_2
    print(f"Hasil dari {angka_1} x {angka_2} adalah {hasil}")
elif operator == "/":
    hasil = angka_1 / angka_2
    print(f"Hasil dari {angka_1} / {angka_2} adalah {hasil}")
else:
    print(f"Operator {operator} tidak tersedia!! Silahkan coba lagi")
print("Program berakhir!")
