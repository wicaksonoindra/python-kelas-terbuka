# Global dan local scope

nama_global = "Otong" # variabel global

# akses variabel global dalam fungsi
def fungsi1():
    print(f"Fungsi menampilkan {nama_global}")

fungsi1()

# akses variabel global dalam loop
for i in range(0,5):
    print(f"loop {i} - {nama_global}")

# percabangan
if True:
    print(f"if menampilkan {nama_global}")

## Variabel local Scope
def fungsi2():
    nama_local = "Ucup" # local variabel

fungsi2()
# print(nama_local) # tidak bisa karena memanggil variabel lokal

## contoh penggunaan
def say_otong():
    print(f"Hello {nama}")

nama = "Otong"
say_otong()

## Contoh 2: merubah variabel global
angka = 0
name = "Ucup"
def ubah(nilai_baru ,nama_baru):
    global angka # fungsi ini mendapat akses merubah variabel
    global name
    angka = nilai_baru
    name = nama_baru

print(f"sebelum = {angka, name}")
ubah(10,"Otong")
print(f"Sesudah = {angka, name}")

## contoh 3: bisa mengambil dan merubah variabel global dalam for dan if
angka = 0
for i in range(0,5):
    angka += i
    angka_dummy = 0
    # print(f"loop ke-{i} = {angka}")

print(angka)
print(angka_dummy)

if True:
    angka = 10
    angka_dummy = 10

print(angka)
print(angka_dummy)
