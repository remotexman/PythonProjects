numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
is_prime = {}
for i in range(len(numbers)):
    if numbers[i] == 1:
        continue
    for j in range(len(numbers)):
        if numbers[j] == 1:
            continue
        if numbers[i] > numbers[j]:
            if numbers[i] % numbers[j] == 0:
                is_prime.update({numbers[i]: False})
                break
        else:
            is_prime.update({numbers[i]: True})
            break
for i, k in is_prime.items():
    if k:
        primes.append(i)
    else:
        not_primes.append(i)
print('Список простых чисел: ', primes)
print('Список составных чисел: ', not_primes)
