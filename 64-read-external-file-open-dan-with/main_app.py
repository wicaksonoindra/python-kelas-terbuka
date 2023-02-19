'''Tutorial membaca file eksternal'''
import os
os.system("cls")

print(3*"=", " Membaca file txt ", 3*"=")
file = open("data.txt",mode="r") # harus di tutup jika sudah mengolah

print(f"status read: {file.readable()}")
print(f"status write: {file.writable()}")

## baca seluruh file
print(file.read())

## baca perbaris file
# print(file.readline(),end="") # baca baris pertama
# print(file.readline(),end="") # baca baris kedua
# print(file.readline()) # baca baris ketiga

## baca semua baris sebagai list
# print(file.readlines())

print(f"apakah file sudah di close: {file.closed}")
file.close()
print(f"apakah file sudah di close: {file.closed}")


## salah satu teknik membuka file di python
print("\n",3*"=", " Membaca file txt dengan with ", 3*"=")
with open("data.txt",mode="r") as file: # tidak harus menutup file karena akan tertutup sendiri
    content = file.readline()
    print(content,end="")
    print(f"apakah file sudah di close: {file.closed}")

print(f"apakah file sudah di close: {file.closed}")
