import random
import threading
import time

class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        for i in range(100):
            addition_cash = random.randint(50, 500)
            self.balance += addition_cash
            print(f'Пополнение:{addition_cash}.Баланс:{self.balance}.')
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            time.sleep(0.001)


    def take(self):
        for i in range(100):
            withdrawal_cash = random.randint(50, 500)
            print(f'Запрос на {withdrawal_cash}')
            if withdrawal_cash <= self.balance:
                self.balance -= withdrawal_cash
                print(f'Снятие:{withdrawal_cash}.Баланс:{self.balance}.')
            else:
                print('Запрос отклонён, недостаточно средств')
                self.lock.acquire()


bk = Bank()

thread1 = threading.Thread(target=Bank.deposit, args=(bk,))
thread2 = threading.Thread(target=Bank.take, args=(bk,))

thread1.start()
thread2.start()
thread1.join()
thread2.join()
print(f'Итоговый баланс: {bk.balance}')

