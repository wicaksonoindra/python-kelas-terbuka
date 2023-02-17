# Menduplikat List

a = ["Ucup","Otong","Dudung"]
print(f"a = {a}")

b = a # Pass by refrence
print(f"b = {b}")

# Merubah member dari a
# Ini akan merubah kedua list
a[1] = "Michael"
b.sort()
print(f"a = {a}")
print(f"b = {b}")

# Address dari kedua list
print(f"Address a = {hex(id(a))}")
print(f"Address b = {hex(id(b))}")

# Menduplikat list dengan copy
print("Membuat List C dengan a.copy")
c = a.copy() # akan mendapatkan list baru dengan Address yang berbeda sehingga tidak akan saling pengaruhi
print(f"Address a = {hex(id(a))}")
print(f"Address b = {hex(id(b))}")
print(f"Address c = {hex(id(c))}")

print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")

print("Ubah data 0")
c[0] = "Dadang"
print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")
