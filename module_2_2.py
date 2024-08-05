first=input('Введите 1-ое число: ')
second=input('Введите 2-ое число: ')
third=input('Введите 3-ое число: ')
# print(first,second,third)
if first==second and first==third:
    print(3)
elif first==second or second==third or first==third:
    print(2)
else:
    print(0)
