class Saloon:
    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine
        self.person = 0

    def print_atri(self):
        print(self.name, end=" ")
        print(self.cuisine, end=" ")
        print(self.person)

    def open(self):
        print(f"{self.name} Открыт")

    def coll_person(self, num_person):
        self.person = num_person
        return self.person

    def sum_person(self, num_person):
        self.person += num_person
        return self.person


class User:
    def __init__(self, name, age, nic):
        self.name = name
        self.age = age
        self.nic = nic
        self.point = 0

    def welcome(self):
        print(f"Hello {self.name}")

    def data(self):
        print("name", self.name, end=", ")
        print("age", self.age, end=", ")
        print("game nic", self.nic, end=", ")
        print("point", self.point)

    def point_new(self, point):
        self.point = point
        return self.point

    def point_del(self):
        self.point = 0
        return self.point
