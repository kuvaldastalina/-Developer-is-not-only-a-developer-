number_of_floors = 1
new_floor = 1
class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = int(number_of_floors)

    def go_to(self, new_floor):
        int(new_floor)
        if new_floor > self.number_of_floors or new_floor < 1:
            print(f"В доме {self.name} не сеществует этажа под № {new_floor}")
        else:
            for i in range(1, new_floor + 1):
                print(i)


x = House('ЖК Эльбрус', 30)
y = House('Домик в деревне', 2)
x.go_to(12)
y.go_to(7)
