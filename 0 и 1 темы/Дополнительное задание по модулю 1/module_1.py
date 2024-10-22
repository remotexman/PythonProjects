grades = [[5, 3, 3, 5, 4],
          [2, 2, 2, 3],
          [4, 5, 5, 2],
          [4, 4, 3],
          [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
dict_of_avg = {}

sorted_list_of_students = sorted(list(students))
dict_of_avg.update({sorted_list_of_students[0]: (sum(grades[0]) / grades[0].__len__()),
                    sorted_list_of_students[1]: (sum(grades[1]) / grades[1].__len__()),
                    sorted_list_of_students[2]: (sum(grades[2]) / grades[2].__len__()),
                    sorted_list_of_students[3]: (sum(grades[3]) / grades[3].__len__()),
                    sorted_list_of_students[4]: (sum(grades[4]) / grades[4].__len__())})
print(dict_of_avg)