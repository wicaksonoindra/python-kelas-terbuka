'''Default Argument'''

# Contoh 1
def say_hello(nama = "Ganteng"):
    print(f"Haloo {nama}!")

say_hello("Ucup")
say_hello()

# Contoh 2
def sapa_dia(nama, pesan = "Whats upp?!"):
    print(f"Hai {nama}, {pesan}")

sapa_dia("Dudung","Hai ganteeeng")
sapa_dia("Otong")

# Contoh 3
def hitung_pangkat(angka, pangkat=2):
    return angka**pangkat

print(hitung_pangkat(2,4))
hasil = hitung_pangkat(pangkat=3, angka=5)
print(hasil)

# Contoh 4
def fungsi(input1=1,input2=2,input3=3,input4=4):
    hasil = input1+input2+input3+input4
    return hasil

print(fungsi())
print(fungsi(input3=10))
