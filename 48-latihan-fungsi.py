'''Latihan Fungsi'''

import os

# Program menghitung luas dan keliling persegi panjang
# Membuat header program
# os.system("clear")
# os.system("cls")
# print(f"{'PROGRAM MENGHITUNG LUAS':^40}")
# print(f"{'DAN KELILINGI PERSEGI PANJANG':^40}")
# print(f"{'-'*40:^40}")
#
# # Mengambil user input
# LEBAR = int(input("Masukkan nilai lebar: "))
# PANJANG = int(input("Masukkan nilai panjang: "))
#
# # Program menghitung luas
# LUAS = PANJANG*LEBAR
# KELILING = 2*(PANJANG+LEBAR)
#
# # Tampilkan hasilnya
# print(f"hasil perhitungan luas = {LUAS}")
# print(f"hasil perhitungan keliling = {KELILING}")

def header():
    '''fungsi header'''
    os.system("cls")
    print(f"{'PROGRAM MENGHITUNG LUAS':^40}")
    print(f"{'DAN KELILING PERSEGI PANJANG':^40}")
    print(f"{'-'*40:^40}")

def input_user():
    lebar = int(input("Masukkan nilai lebar: "))
    panjang = int(input("Masukkan nilai panjang: "))
    return lebar,panjang

def hitung_luas(lebar,panjang):
    '''fungsi luas'''
    return lebar*panjang

def hitung_keliling(lebar,panjang):
    '''fungsi keliling'''
    return 2*(lebar+panjang)

def display(message,value):
    '''fungsi display'''
    print(f"hasil perhitungan {message} = {value}")

def fungsi_opsi():
    print("Opsi: \n0.Luas dan Keliling \n1.Luas \n2.Keliling")
    opsi = input("Masukkan opsi (0,1,2) = ")
    return opsi

# Program Utama
while True:
    header()
    OPSI = fungsi_opsi()
    if OPSI == "0":
        LEBAR,PANJANG = input_user()
        LUAS = hitung_luas(LEBAR,PANJANG)
        KELILING = hitung_keliling(LEBAR,PANJANG)
        display("Hasil perhitungan LUAS",LUAS)
        display("Hasil perhitungan keliling",KELILING)
    elif OPSI == "1":
        LEBAR,PANJANG = input_user()
        LUAS = hitung_luas(LEBAR,PANJANG)
        display("Hasil perhitungan luas",LUAS)
    elif OPSI == "2":
        LEBAR,PANJANG = input_user()
        KELILING = hitung_keliling(LEBAR,PANJANG)
        display("Hasil perhitungan keliling",KELILING)
    else:
        "OPSI TIDAK DI TEMUKAN"

    isContinue = input("Apakah lanjut (y/n)? ")
    if isContinue == "n":
        break

print("Program Selesai, Terima kasih!")
