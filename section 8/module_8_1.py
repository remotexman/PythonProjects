def add_everything_up(a, b):

    try:
        sum = a + b
        
    except TypeError:
        return str(a) + str(b)

    else:
        return sum

print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))