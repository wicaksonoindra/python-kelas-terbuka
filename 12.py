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
