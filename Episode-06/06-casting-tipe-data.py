# casting tipe data, merupakan merubah dari suatu tipe data ke tipe data lain

## INTEGER
print("====INTEGER====")
data_int = 9;
print("data =", data_int, "type =", type(data_int))

data_float = float(data_int)
print("data =", data_float, "type =", type(data_float))

data_str = str(data_int)
print("data =", data_str, "type =", type(data_str))

data_bool = bool(data_int) # akan false jika int=0
print("data =", data_bool, "type =", type(data_bool))

## FLOAT
print("====FLOAT====")
data_float = 9.9;
print("data =", data_float, "type =", type(data_float))

data_int = int(data_float)
print("data =", data_int, "type =", type(data_int))

data_str = str(data_float)
print("data =", data_str, "type =", type(data_str))

data_bool = bool(data_float) # akan false jika int=0
print("data =", data_bool, "type =", type(data_bool))

## BOOLEAN
print("====BOOLEAN====")
data_bool = True;
print("data =", data_bool, "type =", type(data_bool))

data_int = int(data_bool)
print("data =", data_int, "type =", type(data_int))

data_str = str(data_bool)
print("data =", data_str, "type =", type(data_str))

data_float = float(data_bool) # akan false jika int=0
print("data =", data_float, "type =", type(data_float))

## STRING
print("====STRING====")
data_str = "10";
print("data =", data_str, "type =", type(data_str))

data_int = int(data_str)
print("data =", data_int, "type =", type(data_int))

data_bool = bool(data_str)
print("data =", data_bool, "type =", type(data_bool))

data_float = float(data_str)
print("data =", data_float, "type =", type(data_float))
