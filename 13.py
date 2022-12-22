# BITWISE, operasi biner

a = 9
b = 5

# bitwise OR (|)
c = a | b
print('\n ========OR========')
print('nilai :',a,',  binary :', format(a, '08b'))
print('nilai :',b,',  binary :', format(b, '08b'))
print('------------------------------- (|)')
print('nilai :',c,', binary :', format(c, '08b'))

# bitwise AND (&)
c = a & b
print('\n ========AND========')
print('nilai :',a,', binary :', format(a, '08b'))
print('nilai :',b,', binary :', format(b, '08b'))
print('------------------------------- (&)')
print('nilai :',c,', binary :', format(c, '08b'))

# bitwise XOR (^)
c = a ^ b
print('\n ========XOR========')
print('nilai :',a,',  binary :', format(a, '08b'))
print('nilai :',b,',  binary :', format(b, '08b'))
print('------------------------------- (^)')
print('nilai :',c,', binary :', format(c, '08b'))

# bitwise NOT (~)
c = ~a
print('\n ========NOT========')
print('nilai :',a,', binary :', format(a, '08b'))
print('------------------------------- (~)')
print('nilai :',c,', binary :', format(c, '08b'))
print('------------------------------- (^)')
d = 0b00001001
e = 0b11111111
print('nilai :',e^d,', binary: ', format(e^d,'-8b'))

# Shifting
## Shift right(>>)
c = a >> 3
print('\n ========SHIFT RIGHT >>========')
print('nilai :',a,', binary :', format(a, '08b'))
print('------------------------------- (>>)')
print('nilai :',c,', binary :', format(c, '08b'))

## Shift Left(<<)
c = a << 3
print('\n ========SHIFT LEFT <<========')
print('nilai :',a,', binary :', format(a, '08b'))
print('------------------------------- (<<)')
print('nilai :',c,', binary :', format(c, '08b'))
