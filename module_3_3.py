def print_params (a=1, b='строка', c=True):
    print(a,b,c)


print_params()
print_params(2,3)
print_params(2,c=22)
print_params(b=25)
print_params(c=[1,2,3])
values_list=[2,True,'best']
values_dict = {'a': 4, 'b': 5.4, 'c': 'small'}
#####################print(*values_list)
#####################print(**values_dict) почему не работает print () с распаковкой для словерей?
print_params(*values_list)
print_params(**values_dict)
#################################
values_list2=[54.32,'Строка']
print_params(*values_list2,42) ## ошибка продстановки pycharm?








