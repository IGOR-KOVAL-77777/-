########################### словари
my_dict={'Igor': 1965, 'Masha': 2000, 'Sasha':2012, 'Vera':1980}
print(my_dict)
print(my_dict['Masha'])
print(my_dict.get('Dasha','отсутствует'))
my_dict.update({'Oleg':2001, 'Pol':2002})
print(my_dict)
print(my_dict.pop('Oleg'))
print(my_dict)
###################### множества
my_set={1,2,2,'Igor','Igor','Masha',24.67}
print(my_set)
my_set.add(77)
my_set.add(88)
my_set.discard('Igor')
print(my_set)