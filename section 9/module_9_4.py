import random
from os import write

first = 'Мама мыла раму'
second = 'Рамена мало было'
print(list(map(lambda x, y: x == y, first, second)))


def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, 'a', encoding='utf-8') as f:
            for data in data_set:
                f.write(f'{str(data)}\n')
            f.close()
    return write_everything

write = get_advanced_writer('test_file.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

class MysticBall:
    def __init__(self, *words):
        self.words = words

    def __call__(self, *args, **kwargs):
        return random.choice(self.words)

first_ball = MysticBall('Яблоко', 'Ананас', 'Апельсин', 'Груша')
print(first_ball())
print(first_ball())
print(first_ball())
print(first_ball())