# 1. Mode write
# dia akan membuat file baru jika tidak ada, lalu akan menimpa atau overwrite isinya

with open("data1.txt",'w',encoding="utf-8") as file:
    file.write("jon si jhonny")

with open("data1.txt",'w',encoding="utf-8") as file:
    file.write("ucup surucup")

with open("data1.txt",'w',encoding="utf-8") as file:
    file.write("overwrite")

# 2. Mode append
with open("data2.txt",'w',encoding="utf-8") as file:
    file.write("jon si jhonny\n")

with open("data2.txt",'a',encoding="utf-8") as file:
    file.write("ucup surucup\n")

with open("data2.txt",'a',encoding="utf-8") as file:
    file.write("tambah lagi dengan append\n")

# 3. Mode r+
with open("data3.txt",'w',encoding="utf-8") as file:
    file.write("data ke 3\n")

with open("data3.txt",'r+',encoding="utf-8") as file:
    file.write("baris-1 \n")
    file.write("baris-2 \n")
    file.write("baris-3 \n")

with open("data3.txt",'r+',encoding="utf-8") as file:
    data = file.read()
    print(data)

with open("data3.txt",'r+',encoding="utf-8") as file:
    file.write("otong") # menimpa isi teks sesuai dengan panjang data
