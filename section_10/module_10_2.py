import threading
import time


class Knight(threading.Thread):
    def __init__(self,  name, power):
        super().__init__()
        self.name = name
        self.power = power

    def count_battles(self, name, power, enemies=100):
        days = 0
        while enemies:
            enemies -= power
            time.sleep(1)
            days += 1
            print(f'{name} сражается {days} дней(дня)..., осталось {enemies} воинов')
        print(f'{name} одержал победу спустя {days} дней(дня)!')

    def run(self):
        print(f'{self.name}, на нас напали!')
        self.count_battles(self.name, self.power)

first_knight = Knight('Sir Lancelot', 10)
first_knight.start()
second_knight = Knight('Sir Galahad', 20)
second_knight.start()
first_knight.join()
print('Все битвы закончились!')