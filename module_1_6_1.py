grades=[[5,3,3,5,4],[2,2,2,3],[4,5,5,2],[4,4,3],[5,5,5,4,5]] # список
students={'Jonny','Bilbo','Steve','Khendrik','Aaron'}   #множество
print(students, type(students))
l_students=list(students) # перевод в список
print(l_students, type(l_students))
print(l_students.sort(), l_students) # сортировка списка
## l_students=sorted(students) # функция sorted сразу преобразует множество в список?!
## print(l_students, type (l_students))
l_grades=[sum(grades[0])/len(grades[0]),sum(grades[1])/len(grades[1]),sum(grades[2])/len(grades[2]),sum(grades[3])/len(grades[3]),sum(grades[4])/len(grades[4])]
###################w=grades[0]
###################ww=sum(w)/len(w)
#####################print(ww,type(ww))
print(l_grades, type(l_grades), type(l_grades[0]))
dictionary= dict( [ [l_students[0],l_grades[0]],[l_students[1],l_grades[1]],[l_students[2],l_grades[2]],[l_students[3],(l_grades[3])],[l_students[4],l_grades[4]] ] )
print(dictionary, type(dictionary))
