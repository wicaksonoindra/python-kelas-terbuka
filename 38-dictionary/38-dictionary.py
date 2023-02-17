# List -> array, mengakses data menggunakan index
data_list = ['ucup','otong','dudung']
print(data_list[0])

# Dictionary (dict) -> associative array
# Akses data nya menggunakan identifier -> key

data_dict = {
'key':'value',
'cp':'ucup',
'tg':'otong',
'dg':'dudung',
'nmbr':100,
'list':data_list
}
print(data_dict['tg']) # akan memanggil otong
print(data_dict['nmbr'])
print(data_dict['list'])
