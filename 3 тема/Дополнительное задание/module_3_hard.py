data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    'Hello',
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

summ = 0
def calculate_structure_sum(data):
    global summ
    for i in data:
        if isinstance(i, int):
            summ += i
        elif isinstance(i, str):
            summ += len(i)
        elif isinstance(i, list):
            calculate_structure_sum(i)
        elif isinstance(i, tuple):
            calculate_structure_sum(list(i))
        elif isinstance(i, dict):
            calculate_structure_sum(list(i.items()))
        elif isinstance(i, set):
            calculate_structure_sum(list(i))
    return summ

print(calculate_structure_sum(data_structure))