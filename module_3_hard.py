def calculate_structure_sum(x):
    global res
    for z in x:
        #print(z, type(z))
        if isinstance(z, int | bool):
            res += z
        elif isinstance(z, str):
            res += len(z)
        elif isinstance(z, list | tuple | set):
            calculate_structure_sum(z)
        elif isinstance(z, dict):
            calculate_structure_sum(z.keys())
            calculate_structure_sum(z.values())
    return res


res = 0
data_structure = [[1, 2, 3], {'a': 4, 'b': 5}, (6, {'cube': 7, 'drum': 8}), "Hello",
                  ((), [{(2, 'Urban', ('Urban2', 35))}])]
result = calculate_structure_sum(data_structure)
print(result)
############ Т.к. каждая структура может содержать в себе ещё несколько элементов, можно использовать параметр *args
############ ПРОВЕРЯЮЩЕМУ ПРЕПОДАВАТЕЛЮ:
############ К СОЖАЛЕНИЮ Я ТАК И НЕ ПОНЯЛ: КАКИМ ОБРАЗОМ ЗДЕСЬ МОЖНО ПРИМЕНИТЬ *args