#tipe data: Angka Satuan(integer)
data_integer = 1 #automatis  memberikan tipe data tidak seperti bahasa lain
print("data: ", data_integer)
print("- bertipe :", type(data_integer))

#tipe data: Angka dengan koma(float)
data_float = 1.5
print("data: ", data_float)
print("- bertipe :", type(data_float))

#tipe data: kumpulan karakter (String)
data_string = "si ucup 10"
print("data: ", data_string)
print("- bertipe :", type(data_string))

#tipe data: biner true/false(boolean)
data_bool = True
print("data: ", data_bool)
print("- bertipe :", type(data_bool))

## tipe data khusus
# bilangan kompleks
data_complex = complex(5,6)
print("data: ", data_complex)
print("- bertipe :", type(data_complex))

# tipe data dari bahasa C
from ctypes import c_double, c_char
data_c_double = c_double(10.5)
print("data: ", data_c_double)
print("- bertipe :", type(data_c_double))
