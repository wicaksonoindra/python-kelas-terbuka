# Looping Dictionary

teman_teman = {
"cup":"ucup surucup",
"tong":"otong surotong",
"dung":"dudung surudung",
"sep":"asep si kasyep",
"cuy":"ucuy surucuy"
}

# Looping first try(yang keluar key nya)
for teman in teman_teman:
    print(teman)

# Operator mengambil item/iterables
keys = teman_teman.keys()
print(keys)

for key in teman_teman.keys():
    # print(key) # print key nya saja
    print(teman_teman.get(key)) # print value

values = teman_teman.values()
print(values)

for value in teman_teman.values():
    print(value)

items = teman_teman.items()
print(items)

for item in teman_teman.items():
    print(item)

for key,value in teman_teman.items():
    print(f"key = {key}, value = {value}")
