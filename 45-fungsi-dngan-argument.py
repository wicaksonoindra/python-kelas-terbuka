'''
Fungsi dengan argument(input)
template:
def nama_fungsi(argument/parameter/input):
    badan fungsi
'''

def hello_world(nama):
    '''fungsi hello_world menerima input dengan variable nama'''
    print(f"Selamat datang dunia wahai {nama}")

hello_world("ucup")
hello_world("asyep")

# Program tambah
def tambah(angka1,angka2):
    '''fungsi tambah'''
    hasil = angka1 + angka2
    print(f"{angka1} + {angka2} = {hasil}")

tambah(1,5)
tambah(100000,1)

def say_hi(list_peserta):
    '''Fungsi say hi'''
    data_peserta = list_peserta.copy()
    for peserta in data_peserta:
        print(f"Yang terhormat {peserta}")

anggota_boyband = ["Ucup","Otong","Dudung"]

say_hi(anggota_boyband)
