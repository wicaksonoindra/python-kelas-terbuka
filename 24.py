# Perulangan (loop)

# for kondisi:
#     aksi

# Dengan LIST
angka2_list = [0,1,2,3,4] # List
print(angka2_list)

for i in angka2_list:
    print(f"i sekarang -> {i}")
print("Akhir dari program 1\n")

# Dengan Range
angka2_range = range(5)

for i in angka2_range:
    print(f"i sekarang -> {i}")
print("Akhir dari program 2\n")

angka2_range = range(1,10)

for i in angka2_range:
    print(f"i sekarang -> {i}")
print("Akhir dari program 3\n")

# Menggunakan String
data_str = "Saya ganteng abieess"

for huruf in data_str:
    print(huruf)
print("Akhir dari program 4\n")
