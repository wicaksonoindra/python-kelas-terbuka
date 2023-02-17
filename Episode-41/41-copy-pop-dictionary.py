# Copy Dictionary

teman_teman ={
"cup":"ucup surucup",
"tong":"otong surotong",
"dung":"dudung surudung",
"sep":"asep si kasyep",
"cuy":"ucuy surucuy"
}

friends = teman_teman.copy() # Jika tidak menggunakan copy, maka friends akan merujuk ke refrensi yang sama (alamat yang sama)
print(f"teman-teman: {teman_teman}\n")
print(f"friends: {friends}\n")

teman_teman["cup"] = "ucup si keren"
print(f"teman-teman: {teman_teman}\n")
print(f"friends: {friends}\n")

# Pop Dictionary
dataAsep = friends.pop("sep") # mengambil value dari key "sep"
print(f"dataAsep = {dataAsep}")
print(f"friends = {friends}") # data sep hilang karena di pop

# popitem Dictionary (yang terakhir)
dataTerakhir = friends.popitem() # mengambil key dan value data terakhir
print(f"data terakhir = {dataTerakhir}")
print(f"friends = {friends}") # data terakhir akan hilang
