data_angka = [1,5,2,6,8,4,4,4,4,4,4,4,4,5,3,1,4,6,2,0,3,3,3,3,3,3,3]

print(f"data angka = \n{data_angka}")

# Count data
jumlah_data_4 = data_angka.count(4)
jumlah_data_3 = data_angka.count(3)
print(f"jumlah angka 4 = {jumlah_data_4}")
print(f"jumlah angka 3 = {jumlah_data_3}")

# ambil posisi data (index)
data = ["Ucup","Otong","Dudung","Ujang"]
print(f"data = {data}")

index_dudung = data.index("Dudung")
index_ujang = data.index("Ujang")
print(f"index Dudung = {index_dudung}")
print(f"index Ujang = {index_ujang}")

# Mengurutkan list
print(f"Data angka sebelum sort = \n{data_angka}")
data_angka.sort()
print(f"Data angka setelah sort = \n{data_angka}")

print(f"Data sebelum di sort = \n{data}")
data.sort()
print(f"Data setelah sort = \n{data}")

# Reverse list
data_angka.reverse()
data.reverse()
print(f"data angka di reverse = {data_angka}")
print(f"data di reverse = {data}")
