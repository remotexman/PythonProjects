def print_params(a = 1, b = 'string', c = True):
    print(a, b, c)
print_params(2, 'hello')
print_params(2, 'hello', False)
print_params(2)
print_params()
print_params(b=25)
print_params(c=[1, 2 , 3])

value_list = [33, (1, 2, 3), 'abcdefgh']
value_dict = {'a': 21, 'b': 'qwerty', 'c': False}
print_params(*value_list)
print_params(**value_dict)
value_list_2 = [[2, 2, 2], 'rtp']
print_params(*value_list_2, 42)