# Operator dalam bentuk Methods

## Merubah case dari string

# Merubah semua ke upper case
salam = "bro!"
print("normal = " + salam)
salam = salam.upper()
print("upper = " + salam)

# Merubah semua ke lower case
alay = "aKu KecE AbIeeEzzzz"
print("normal = " + alay)
alay = alay.lower()
print("Lower = " + alay)

## Pengecekan dengan isX methog
# contoh pengecekan lower case
salam = "sist"
apakah_lower = salam.islower() # hasilnya bool
print(salam + " is lower = " + str(apakah_lower))
apakah_upper = salam.isupper() # hasilnya bool
print(salam + " is upper = " + str(apakah_upper))

# isalpha() <-- untuk mengecek semuanya huruf
# isalnum() <-- huruf dan angka
# isdecimal() <-- angka saja
# isspace() <-- spasi,tab,newline
# istitle() <-- semua kata dimulai dengan huruf besar

judul = "It Is Okay Not To Be Orkay"
cek_judul = judul.istitle()
print(judul + " is title? " + str(cek_judul))

## Cek Komponen startswith() endswith() <-- keren
cek_start = "Sangjangnim Oppa".startswith("Sangjangnim")
print("start = " + str(cek_start))

cek_end = "Sangjangnim Oppak".endswith("Oppak")
print("end = " + str(cek_end))

## Penggabungan Komponen join() split()
pisah = ['aku', 'sayang', 'kamu']
gabungan = ','.join(pisah)
print(pisah)
print(gabungan)
gabungan = ' '.join(pisah)
print(gabungan)

gabungan = ' ehm '.join(pisah)
print(gabungan)

gabungan = "akuehmsayangehmkamu"
print(gabungan.split('ehm'))

## Alokasi karakter rjust(), ljust(), center()
print(5*"=" + "data" + 5*"=")
kanan = "kanan".rjust(10)
print("'"+kanan+"'")

kiri = "kiri".ljust(10)
print("'"+kiri+"'")

tengah = "tengah".center(20,":")
print("'"+tengah+"'")

# Kebalikannya -> strip()
tengah = tengah.strip(":") # menghilangkan tanda :
print("'"+tengah+"'")
