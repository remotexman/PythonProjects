from itertools import count

calls = 0
def count_calls():
    global calls
    calls += 1

def string_info(string):
    count_calls()
    return len(string), string.upper(), string.lower()

def is_contains(string, list_to_search):
    count_calls()
    for i in list_to_search:
        if string.upper() == i.upper():
            return True
        else:
            return False

print(string_info('Apple'))
print(string_info('Pineapple'))
print(is_contains('Qwe', ['QwE', 'qWee', 'WWE']))
print(is_contains('fork', ['work', 'uncork']))
print(calls)

