class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'

    def __bool__(self):
        return self.number_of_floors


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

#################################################### ВЕРОЯТНО В УСЛОВИИ ЗАДАЧИ ОШИБКА
print(h1)
print(h2)
####################################################
#__str__
print(str(h1))
print(str(h2))

 #__len__
print(len(h1))
print(len(h2))
