# OPERASI ARITMATIKA

a = 10
b = 3

print("\n===PERTAMBAHAN===")
hasil = a + b
print(a, ' + ',b, ' = ', hasil)

print("\n===PENGURANGAN===")
hasil = a - b
print(a, ' - ',b, ' = ', hasil)

print("\n===PERKALIAN===")
hasil = a * b
print(a, ' * ',b, ' = ', hasil)

print("\n===PEMBAGIAN===")
hasil = a / b
print(a, ' / ',b, ' = ', hasil) #hasil pembagian akan bertipe data float

print("\n===EKSPONEN(PANGKAT)===")
hasil = a ** b
print(a, ' ** ',b, ' = ', hasil)

print("\n===MODULUS(SISA BAGI)===")
hasil = a % b
print(a, ' % ',b, ' = ', hasil)

print("\n===FLOOR DIVISION(KEBALIKAN MODULUS)===")
hasil = a // b
print(a, ' // ',b, ' = ', hasil)

# PRIORITAS OPERASI, operational precedence
print("\n===PRIORITAS OPERASI===")
"""
Urutan Prioritas
1. ()
2. Eksponen **
3. Perkalian dan teman teman * / ** % //
4. Pertambahan dan pengurangan + -
"""
x = 3
y = 2
z = 4

hasil = x ** y * z + x / y - y % z // x
print(x,'**',y,'*',z,'+',x,'/',y,'-',y,'%',z,'//',x,' = ', hasil)
