def custom_write(file_name, strings):
    string_positions = {}
    file = open(file_name, 'w', encoding='utf-8')
    s = 0
    for string in strings:
        s += 1
        string_positions[tuple([s, file.tell()])] = string
        file.write(f'{string}\n')
    file.close()
    return string_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)

for elem in result.items():
    print(elem)
