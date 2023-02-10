'''Type hints untuk fungsi'''
# bentuk standar fungsi yang sudah dipelajari
'''
studi kasus
def fungsi(parameter):
    hasil = parameter**2
    print(hasil)

fungsi(1)
fungsi("Ucup")
fungsi(True)
'''
import string
# penggunaan type hints

def sepuluh_pangkat(argument:int) -> int:
    output = 10**argument
    return output
HASIL = sepuluh_pangkat(2)
print(HASIL)

def display(argument:string):
    print(argument)

display("Ucup")

import os
hasil = os.system("clear")
print(hasil)
