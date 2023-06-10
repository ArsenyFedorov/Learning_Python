class Saloon:
    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine

    def print_atri(self):
        print(self.name, end=" ")
        print(self.cuisine)

    def open(self):
        print(f"{self.name} openit")


class User:
    def __init__(self, name, age, nic):
        self.name = name
        self.age = age
        self.nic = nic

    def welcome(self):
        print(f"Hello {self.name}")

    def data(self):
        print("name", self.name, end=", ")
        print("age", self.age, end=", ")
        print("game nic", self.nic)
