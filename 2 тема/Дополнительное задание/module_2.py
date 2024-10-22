import random
list_of_numbers = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
first_number = random.choice(list_of_numbers)
list_of_dividers = []
list_with_result = []
for i in range(3, first_number + 1):
    if first_number % i == 0:
        list_of_dividers.append(i)
for i in list_of_dividers:
    for j in range(1, i):
        if j < i - j:
            list_with_result.append(j)
            list_with_result.append(i - j)
str_numbers = [str(i) for i in list_with_result]
result = ''.join(str_numbers)
print('Число в первом поле: ', first_number)
print('Число во втором поле: ', result)



