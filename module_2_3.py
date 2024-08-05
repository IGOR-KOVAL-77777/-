my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
# my_list = [42,69,322,13,0,99,5,9,8,7,6,5]
x = 0
y = my_list[x]
while y >= 0:
    if y > 0: print(y)
    x = x + 1
    if x > len(my_list) - 1:
        print('окончание списка!')
        break
    else:
        y = my_list[x]
        continue
if y < 0: print('встречено отрицательное значение!')
