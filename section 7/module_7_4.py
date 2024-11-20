team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451
task_total = score_1 + score_2
time_avg = round((team1_time + team2_time) / task_total, 1)
if score_1 > score_2 or score_1 == score_2 and team1_time < team2_time:
    challenge_result = 'Победа команды Мастера кода!'
elif score_1 < score_2 or score_1 == score_2 and team1_time > team2_time:
    challenge_result = 'Победа команды Волшебники данных!'
else:
    challenge_result = 'Ничья'
# ---------------------------Использование %-----------------------------------------------------------------------------

print('В команде мастера кода участников: %s' % team1_num)
print('Итого сегодня в командах участников: %(team1)s и %(team2)s' % {'team1': team1_num, 'team2': team2_num})

# ---------------------------Использование format()----------------------------------------------------------------------

print('Команда Волшебники данных решила задач: {score}'.format(score=score_2))
print('Волшебники данных решили задачи за {}'.format(team2_time))

# ---------------------------Использование f-строк-----------------------------------------------------------------------

print(f'Команды решили {score_1} и {score_2} задач')
print(f'Сегодня было решено {task_total} задач, в среднем по {time_avg} секунды на задачу!')

