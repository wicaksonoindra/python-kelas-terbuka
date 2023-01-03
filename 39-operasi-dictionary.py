# Operator dictionary
data_dict = {
"cup":"ucup surucup",
"tong":"otong surotong",
"dung":"dudung surudung"
}

# Panjang dictionary
LENDICT = len(data_dict) # Konstan
print(f"panjang dictionary: {LENDICT}")

# Cek key exist atau tidak
KEY = "cup"
CHECKKEY = KEY in data_dict
print(f"Apakah {KEY} ada di data_dict: {CHECKKEY}")

# Mengakses value (read) dengan get
# print(data_dict["kis"]) # akan arror jika bukan dictionary
print(data_dict.get("cup")) # merupakan dictionarykarena menggunakan get
print(data_dict.get("kis","key tidak ditemukan")) # check key dengan message key tidak ditemukan

# mengupdate data
data_dict["cup"] = "ucup si ganteng"
print(data_dict)
data_dict["sep"] = "asep si kasyep" # menambah
print(data_dict)

data_dict.update({"cup":"ucup surucup"}) # akan merubah isi jika key nya ada
print(data_dict)
data_dict.update({"indraw":"indraw si kerenzz"}) # kalo ga ada akan di add
print(data_dict)

# Mendelete data pada dictionary
del data_dict["indraw"]
print(data_dict)
