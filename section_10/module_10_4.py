import random
import threading
from queue import Queue
import time


class Table:
    def __init__(self, number, guest=None):
        self.number = number
        self.guest = guest


class Guest(threading.Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        time.sleep(random.randint(3, 10))


class Cafe:
    def __init__(self, *tables):
        self.queue = Queue()
        self.tables = tables

    def guest_arrival(self, *guests):
        for guest in guests:
            seated = False
            for table in self.tables:
                if table.guest is None:
                    table.guest = guest
                    guest.start()
                    seated = True
                    print(f'{guest.name} сел(-а) за стол номер {table.number}')
                    break
            if not seated:
                self.queue.put(guest)
                print(f'{guest.name} в очереди')

    def discuss_guests(self):
        while not self.queue.empty() or any(table.guest for table in self.tables):
            for table in self.tables:
                if table.guest and not table.guest.is_alive():
                    print(f'{table.guest.name} покушал(-а) и ушел(ушла)')
                    print((f'Стол номер {table.number} свободен'))
                    table.guest = None

            for table in self.tables:
                if table.guest is None and not self.queue.empty():
                    guest_ = self.queue.get()
                    table.guest = guest_
                    print(f'{guest_.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}')
                    guest_.start()


tables = [Table(number) for number in range(1, 6)]

guests_names = [
    'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
    'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]

guests = [Guest(name) for name in guests_names]

cafe = Cafe(*tables)
cafe.guest_arrival(*guests)
cafe.discuss_guests()