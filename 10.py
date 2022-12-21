# Operasi Komparasi
# Setiap hasil dari operasi komparasi adalah boolean
#>,<,>=,<=,==,!=.is,is not

a = 4
b = 2.1

# LEBIH BESAR DARI >
print('========== Lebih besar dari (>)')
hasil = a > 3
print(a, '>',3, '=', hasil)
hasil = b > 3
print(b, '>',3, '=', hasil)
hasil = b > 2
print(b, '>',2, '=', hasil)

#  KURANG DARI <
print('========== Kurang dari (<)')
hasil = a < 3
print(a, '<',3, '=', hasil)
hasil = b < 3
print(b, '<',3, '=', hasil)
hasil = b > 2
print(b, '<',2, '=', hasil)

#  LEBIH DARI SAMA DENGAN >=
print('========== lebih dari sama dengan (>=)')
hasil = a >= 3
print(a, '>=',3, '=', hasil)
hasil = b >= 3
print(b, '>=',3, '=', hasil)
hasil = b >= 2
print(b, '>=',2, '=', hasil)

#  KURANG DARI SAMA DENGAN <=
hasil = a <= 3
print('========== kurang dari sama dengan (<=)')
print(a, '<=',3, '=', hasil)
hasil = b <= 3
print(b, '<=',3, '=', hasil)
hasil = b <= 2
print(b, '<=',2, '=', hasil)

# sama dengan (==)
print('========== sama dengan (==)')
hasil = b == 4
print(b,'==',4,'=',hasil)

# tidak sama dengan (==)
print('========== sama dengan (!=)')
hasil = b != 4
print(b,'!=',4,'=',hasil)

# 'is' sebagai komparasi object identity
print('========== object identity (is)')
x = 5 # ini adalah assigment membuat object
y = 5
print('nilai x =,',x,'id = ', hex(id(x)))
print('nilai y =,',y,'id = ', hex(id(y)))
hasil = x is y
print('x is y', hasil)

x = 5 # ini adalah assigment membuat object
y = 6
print('nilai x =,',x,'id = ', hex(id(x)))
print('nilai y =,',y,'id = ', hex(id(y)))
hasil = x is y
print('x is y', hasil)

# 'is not' sebagai komparasi object identity
print('========== object identity (is)')
x = 5 # ini adalah assigment membuat object
y = 5
print('nilai x =,',x,'id = ', hex(id(x)))
print('nilai y =,',y,'id = ', hex(id(y)))
hasil = x is not y
print('x is not y', hasil)

x = 5 # ini adalah assigment membuat object
y = 6
print('nilai x =,',x,'id = ', hex(id(x)))
print('nilai y =,',y,'id = ', hex(id(y)))
hasil = x is not y
print('x is not y', hasil)
