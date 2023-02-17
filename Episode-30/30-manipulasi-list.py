## Operasi

# index  0(-3)   1(-2)   2(-1)
data = ["Ucup","Otong","Dudung"]

# Mengambil data dari list
data_0 = data[0]
print(f"data pertama (index 0) = {data[0]}")

data_terakhir = data[-1]
print(f"data terakhir adalah = {data_terakhir}")

data_ucup = data[-3]
print(f"data ucup = {data_ucup}")

# Mengambil info jumlah data list
panjang_data = len(data)
print(f"panjang data = {panjang_data}")

## Manipulasi data list

# Menambahkan item pada list sesuai posisi
print(f"data sebelum ditambah = \n{data}")
data.insert(1,"Asep") # (posisi, data)
print(f"data sesudah ditambah = \n{data}")

# Menambahkan di akhir list
data.append("Jajang")
print(f"data ditambah lagi = \n{data}")

# Menambahkan list dengan list
data_baru = ["Ujang","Usep","Dadang"]
data.extend(data_baru)
print(f"data gabungan = \n{data}")

# Merubah data
# Ubah data 2 otong menjadi michael
data[2] = "Michael"
print(f"data yang dirubah = \n{data}")

# Remove data
data.remove("Ujang")
print(f"Data remove = \n{data}")
# data.remove("usep") akan error karena data tidak ditemukan

# Remove data paling belakang
data.pop()
print(f"data akhir = \n{data}")
data_akhir = data.pop()
print(data_akhir)
