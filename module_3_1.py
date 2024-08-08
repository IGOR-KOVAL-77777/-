calls = 0


def count_calls():
    global calls
    calls = calls + 1


def string_info(string):
    count_calls()
    return (len(string), string.upper(), string.lower())


def is_contains(string, list_to_search):
    count_calls()
    # string=string.upper()
    # print(string)
    s = False
    for i in range(0, len(list_to_search)):
        if string.upper() == list_to_search[i].upper():
            s = True
            break
    return s


print(string_info('Capibara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)
# почему выходят серые наименования аргументов в случае с функцией is_contains ????
# string.upper() почему при применении метод не меняется переменная????