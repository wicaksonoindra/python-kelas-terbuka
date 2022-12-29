# Latihan perulangan membuat segitiga

sisi = 19

# 1. FOR
#Dummy variable
print("\n Segitiga dengan perulangan for")
count = 1
for i in range(sisi):
    print("*"*count)
    count += 1

# 2. WHILE
print("\n Segitiga dengan perulangan while")
count = 1
while True:
    print("*"*count)
    count += 1
    if count > sisi:
        break

# 3. Ganjil saja
print("\n Segitiga Ganjil saja")
count = 1
while True:
    if count%2:
        # Print jika ganjil
        print("*"*count)
        count += 1
    else:
        # Continue jika genap
        count += 1
        continue
    if count > sisi:
        # Akan break jika melebihi sisi
        break

# 4. Segitiga sama sisi
print("\n Segitiga Sama sisi")
count = 1
spasi = int(sisi/2)
while True:
    if count%2:
        # Print jika ganjil
        print(" "*spasi,"+"*count)
        count += 1
        spasi -= 1
    else:
        # Continue jika genap
        count += 1
        continue
    if count > sisi:
        # Akan break jika melebihi sisi
        break
