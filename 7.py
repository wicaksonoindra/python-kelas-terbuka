# Input User
"""
data yang di masukkan pasti string
"""

# STRING(default)
print("\n===STRING===")
data = input("Masukkan data: ")
print("Data: ", data, ", Tipe data anda: ", type(data))

# INTEGER
print("\n===INTEGER===")
angka = int(input("Masukkan angka: "))
print("Data: ", angka, ", Tipe data anda: ", type(angka))

# FLOAT
print("\n===FLOAT===")
angka = float(input("Masukkan angka: "))
print("Data: ", data, ", Tipe data anda: ", type(angka))

# BOOLEAN
print("\n===BOOLEAN===")
biner = bool(int(input("Masukkan nilai boolean: ")))
print("Data: ", biner, ", Tipe data anda: ", type(biner))
