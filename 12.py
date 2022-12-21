# Latihan Logika dan komparasi

# membuat gabungan area rentang dari sebuah angka

# +++++++++3-------------10++++++++++++

inputUser = float(input("Masukkan angka yang bernilai kurang dari 3 \natau \nlebih besar dari 10\n:"))

#++++++++++3--------------------
# Memeriksa angka kurang dari 3
isKurangDari = (inputUser<3)
print("Kurang dari 3 =",isKurangDari)

#--------------10+++++++++
# Memeriksa angka lebih dari 10
isLebihDari = (inputUser > 10)
print("Lebih dari 10 =", isLebihDari)

# +++++++++3-------------10++++++++++++

isCorrect = isKurangDari or isLebihDari
print("Angka yang anda masukkan:",isCorrect)

# -----3++++++++10-------
# Kasus Irisan
print("\n",10*"=","\n")
inputUser = float(input("Masukkan angka yang bernilai kurang dari 3 \ndan \nkurang dari 10\n:"))

# -----3+++++++
# Lebih dari 3
isLebihDari = inputUser > 3
print("Lebih dari 3 =", isLebihDari)

# +++++++10----
# Kurang dari 10
isKurangDari = inputUser < 10
print("Kurang dari 10 =", isKurangDari)

isCorrect = isKurangDari and isLebihDari
print("Angka yang anda masukkan:",isCorrect)

print("\n",15*"=","PR",15*"=","\n")
inputUser = float(input("Soal 1, Masukkan angka: "))
# 1. ---0+++5---8+++11---
## LEBIH DARI 0
isLebihDari0 = inputUser > 0
## KURANG DARI 5
isKurangDari5 = inputUser < 5
isCorrect1 = isLebihDari0 and isKurangDari5

## LEBIH DARI 8
isLebihDari8 = inputUser > 8
## KURANG DARI 11
isKurangDari11 = inputUser < 11
isCorrect2 = isLebihDari8 and isKurangDari11

final = isCorrect1 or isCorrect2
print("Angka yang anda masukkan: ", final)

# 2. +++0---5+++8---11+++
inputUser = float(input("Soal 2, Masukkan angka: "))
## KURANG DARI 0
isKurangDari0 = inputUser < 0
## LEBIH DARI 5
isLebihDari5 = inputUser > 5
## KURANG DARI 8
isKurangDari8 = inputUser < 8
## LEBIH DARI 11
isLebihDari11 = inputUser > 11

isCorrect1 = isLebihDari5 and isKurangDari8
final = isCorrect1 or isKurangDari0 or isLebihDari11
print("Angka yang anda masukkan: ", final)
