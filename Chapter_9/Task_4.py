from Task_1 import Saloon as Sl


class Ice_cream_salon(Sl):
    def __init__(self, name, cuisine, flavors: list):
        super().__init__(name, cuisine)
        self.person = 0
        self.flavors = flavors

    def print_atri(self):
        print(self.name, end=" ")
        print(self.cuisine, end=" ")
        print(self.person)
        print("Вкусы мороженого", *self.flavors)


ice_cream = Ice_cream_salon("ГУМ", "Кафе", ["Ванильное", "Шоколадное", "Пломбир"])

ice_cream.print_atri()
