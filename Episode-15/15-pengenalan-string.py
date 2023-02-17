data = "ini adalah string"
print(data)
print(type(data))

# 1. Cara membuat string

'''
    1. dengan menggunakan single quote '...'
    2. dengan menggunakan double qupte "..."
'''

data = 'menggunakan single quote'
print(data)

data = "menggunakan double quote"
print(data)

print('"Haloo, apaa kabar?"')
print("'Haloo, apaa kabar?'")
print("ini adalah hari jum'at")

# 2. Menggunakan backslash(\)
# Membuat tanda ' menjadi string
print('mari shalat jum\'at')
print('g\'day, isn\'t it?')

# Backslash
print("C:\\user\\Ucup")

# Tab
print("ucup\t\t\totong, semakin jauhan")

# Backspace
print("ucup \botong, jadi deketan")

# Newline
print("baris pertama.\nbaris kedua.") # LF -> Line feed -> unix, macos. linux
print("baris pertama.\rbaris kedua.") # CR -> carrieage return -> commodore, acorn, lisp
print("baris pertama.\r\nbaris kedua.") # CRLF -> Line feed carrieage return -> dipakai oleh windows

# 3. String Literal atau raw
# hati-hati
print('C:\new folder') # akan salah path

# menggunakan raw String
print(r'C:\\newc\t\r\bfolder') # semua akan diabaikan

# multiline literal String
print("""
Nama: Ucup
Kelas: 3 SD
""")

# multiline litreal string dan RAW
print(r"""
Nama: Ucup
Kelas: 3 SD\new normal
Website: www.ucup.com/newID
""")
