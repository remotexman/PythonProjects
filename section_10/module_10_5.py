import multiprocessing
import time


def read_info(name):
    all_data = []
    with open(name, 'r') as file_:
        while file_.readline():
            all_data.append(file_.readline())
    file_.close()



file_names = ['file_1.txt', 'file_2.txt', 'file_3.txt', 'file_4.txt']

start = time.time()
for file in file_names:
    read_info(file)

end = time.time()
print(end - start)

# if __name__ == '__main__':
#     st = time.time()
#     with multiprocessing.Pool(4) as p:
#         p.map(read_info, file_names)
#     en = time.time()
#     print(en - st)


