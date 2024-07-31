immutable_var=1,2,4,True,'solonka'
print(immutable_var, type(immutable_var))
# immutable_var[1]=0
# Traceback (most recent call last):
#  File "C:\Users\Гарик\PycharmProjects\pythonProject\module_1_5.py", line 3, in <module>
#    immutable_var[1]=0
#   ~~~~~~~~~~~~~^^^
# TypeError: 'tuple' object does not support item assignment
# кортеж не поддерживает изменение элементов!!!!!!!!!!!!!!!!
# print(immutable_var, type(immutable_var))
mutable_list=[5,7,True,'solonka','224455']
print(mutable_list, type(mutable_list))
mutable_list[1]=1000
mutable_list[-1]=2244
print(mutable_list, type(mutable_list))
mutable_list[1:4]='**'
print(mutable_list, type(mutable_list))
