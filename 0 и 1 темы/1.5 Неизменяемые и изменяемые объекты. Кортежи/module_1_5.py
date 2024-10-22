immutable_var = ('rabbit', 'cat', 345.9, False)
print(immutable_var)

#immutable_var[0] = 'dog'
#TypeError: 'tuple' object does not support item assignment

mutable_list = [1, 2, 3]
mutable_list[-1] = 99
mutable_list.append('hdd')
print(mutable_list)