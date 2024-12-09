def is_prime(func):
    def wrapper(f, s, th):
        res = f + s + th
        if res <= 1:
            return 'Составное'
        if res == 2:
            return 'Простое'
        if res % 2 == 0:
            return 'Составное'
        for i in range(3, int(res ** 0.5) + 1, 2):
            if res % i == 0:
                return 'Составное'
        return 'Простое'
    return wrapper

@is_prime
def sum_three(first, second, third):
    return first + second + third


result = sum_three(2, 3, 6)
print(result)

