'''Fungsi dengan Kembalian'''
# Template fungsi dengan Kembalian
# def nama_fungsi(argument):
#       badan Fungsi
#       return output

# Fungsi kuadrat
def kuadrat(input_angka):
    output_kuadrat = input_angka**2
    return output_kuadrat

y = kuadrat(3)
print(y)

print(kuadrat(6))

z = 10 + kuadrat(7)
print(z)

# Fungsi tambah
def fungsi_tambah(angka_1,angka_2):
    return angka_1 + angka_2

a = fungsi_tambah(10,8)
print(a)

# Fungsi dengan return banyak
def operasi_matematika(angka_1,angka_2):
    tambah = angka_1 + angka_2
    kurang = angka_1 - angka_2
    kali = angka_1 * angka_2
    bagi = angka_1 / angka_2

    return tambah,kurang,kali,bagi

tam,kur,kal,bag = operasi_matematika(10,5)
print(f"Hasil tambah = {tam}")
print(f"Hasil kurang = {kur}")
print(f"Hasil kali = {kal}")
print(f"Hasil bagi = {bag}")
