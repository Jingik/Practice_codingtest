T = int(input())
default_str = 'long int'
long = 'long '
if T >= 4 :
    number = T // 4
    print((number-1)*long + default_str )
else:
    print(default_str)