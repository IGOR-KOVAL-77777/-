class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        self.new_floor = new_floor
        # print(self.number_of_floors, new_floor)
        if new_floor < 1 or new_floor > self.number_of_floors:
            print('Такого этажа не существует')
        else:
            for i in range(1,new_floor+1):
                print(i)
                i += 1


h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
# print(h1, type(h1), id(h1), id(h1.name), id(h1.number_of_floors))
h1.go_to(5)
h2.go_to(10)
