import threading
import time
from math import floor


def write_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf-8') as f:
        for i in range(1, word_count + 1):
            f.write(f'Какое-то слово № {i}\n')
            time.sleep(0.1)
        f.close()
    print(f'Завершилась запись в файл {file_name}')

start_func = time.time()

write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

end_func = time.time()

print(f'Время затраченное на выполнение функций: {round(end_func - start_func, 2)} секунд')

start_thread = time.time()

thread_1 = threading.Thread(target=write_words, args=(10, 'example5.txt'))
thread_2 = threading.Thread(target=write_words, args=(30, 'example6.txt'))
thread_3 = threading.Thread(target=write_words, args=(200, 'example7.txt'))
thread_4 = threading.Thread(target=write_words, args=(100, 'example8.txt'))

thread_1.start()
thread_2.start()
thread_3.start()
thread_4.start()
thread_3.join()


end_thread = time.time()

print(f'Время затраченное на выполнение потоков: {round(end_thread - start_thread, 2)} секунд')
