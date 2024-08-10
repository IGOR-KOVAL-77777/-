def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print('1.Функция с параметрами по умолчанию:')
print_params()
print_params(2, 3)
print_params(2, c=22)
print_params(b=25)
print_params(c=[1, 2, 3])
values_list = [2, True, 'best']
values_dict = {'a': 4, 'b': 5.4, 'c': 'small'}
#####################print(*values_list)
#####################print(**values_dict) почему не работает print () с распаковкой для словерей?
print('2.Распаковка параметров:')
print_params(*values_list)
print_params(**values_dict)
print('3.Распаковка + отдельные параметры:')
values_list2 = [54.32, 'Строка']
print_params(*values_list2, 42)  ## ошибка продстановки pycharm?
print('Важно!')


def append_to_list(item, list_my=None):
    if list_my is None:
        list_my = []
    list_my.append(item)
    print(list_my)


append_to_list(2)
append_to_list(5)
append_to_list([2, 5])
append_to_list([])








