class Employee:
    def __init__(self, name: str, surname: str, salary: int):
        self.name = name
        self.surname = surname
        self.salary = salary

    def give_raise(self, num: int = 5_000):
        if num >= 0:
            self.salary += num
            return self.salary
        else:
            print("Зарплату нельзя урезать!!!!")
