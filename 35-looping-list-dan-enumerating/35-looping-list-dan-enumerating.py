# looping dari list
# for loop
print("FOR LOOP")
kumpulan_angka = [4,3,2,5,6,1]

for angka in kumpulan_angka:
    print(f"angka = {angka}")

peserta = ["ucup","otong","dadang","diding","dudung"]

for nama in peserta:
    print(f"nama = {nama}")

# for loop dan range
print("\nFOR LOOP DAN RANGE")
kumpulan_angka = [10,5,4,2,6]
panjang = len(kumpulan_angka)

for i in range(panjang):
    print(f"angka = {kumpulan_angka[i]}")

# while
print("\n WHILE LOOP")
kumpulan_angka = [10,5,4,2,6]
panjang = len(kumpulan_angka)

i = 0
while i < panjang:
    print(f"angka = {kumpulan_angka[i]}")
    i+=1

# List Comprehension
print("\nList Comprehension")
data = ["ucup",1,2,3,"otong"]

[print(f"data={i}") for i in data]
angka = [10,5,4,2,6]
angka_kuadrat = [i**2 for i in angka]
print(angka_kuadrat)

# Enumerate
print("\nEnumerate")
data_list = ["ucup",1,2,3,"otong"]

for index,data in enumerate(data_list):
    print(f"index = {index}, data = {data}")
