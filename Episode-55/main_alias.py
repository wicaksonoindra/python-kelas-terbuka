# Module matematika dengan import

from matematika import tambah as add
from matematika import kali as k
from matematika import pangkat as terserah_kalian
# from matematika import * # import from semua

import matematika as math # <--- bias di lakukan

hasil_tambah = add(1,2,3,4,5)
print(f"Hasil tambah = {hasil_tambah}")

hasil_kali = math.kali(1,2,3,4,5)
print(f"Hasil kali = {hasil_kali}")

pangkat_3 = terserah_kalian(3)
print(f"Hasil pangkat 3 = {pangkat_3(3)}")
