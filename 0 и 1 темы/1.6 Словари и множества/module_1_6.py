#Task 1
my_dict = {'Danila': 100, 'Nikita': 250, 'Victor': 500}
print(my_dict)
print(my_dict['Danila'])
print(my_dict.get('Maxim', 'Without Error'))
my_dict['Fail'] = 430
my_dict['Vladimir'] = 700
temp = my_dict.pop('Nikita')
print(temp)
print(my_dict)

#Task 2
my_set = {1, 2, 3, 4, 'apple', 'banana', 4, 3, 'banana'}
print(my_set)
my_set.add(7)
my_set.add('strawberry')
my_set.discard('apple')
print(my_set)