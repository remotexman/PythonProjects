def check(email):
    list_of_ends = ['.com', '.ru', '.net']
    current = False
    for i in list_of_ends:
        if email.endswith(i) and '@' in email:
            current = True
        else:
            continue
    return current
def send_email(message, recipient, sender = 'university.help@gmail.com'):
    check_for_recipient = check(recipient)
    check_for_sender = check(sender)
    if not check_for_recipient or not check_for_sender:
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
    elif sender == recipient:
        print('Нельзя отправить письмо самому себе!')
    elif sender == 'university.help@gmail.com':
        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}.')
    else:
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.')

send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban@teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban@teacher@mail.ru', sender='urban@teacher@mail.ru')

