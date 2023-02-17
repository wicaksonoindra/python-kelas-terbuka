# import

# fungsinya adalah untuk mengabmbil program dari file eksternal .py

# 1. Untuk menyambung program dari eksternal
import program_print
import program_ucup

# 2. Import dengan data
import variabel
import kucuy

# data ada di namespace variabel
print(variabel.data)
print(kucuy.data)

# 3. Import dengan fungsi
import matematika
hasil = matematika.tambah(4,5)
print(f"Hasil = {hasil}")
