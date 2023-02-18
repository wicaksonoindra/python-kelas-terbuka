'''Standard Library'''

import datetime

data_Waktu = datetime.datetime.now()
print(f"datetime now: {data_Waktu}")
print(f"tahun: {data_Waktu.year}")
print(f"hari: {data_Waktu.strftime('%A')}")

from collections import Counter

data = ["a","b","c","d","a","d","e"]
data_count = Counter(data)
print(f"data count = {data_count}")
print(f"jumlah a = {data_count['a']}")
print(f"jumlah d = {data_count['d']}")

import io

file = io.open("file_text.txt","r")
print(file.read())
