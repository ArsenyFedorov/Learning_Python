from Task_1 import User as UR


class Admin(UR):
    def __init__(self, name, age, nic):
        super().__init__(name, age, nic)
        self.liberty = Liberty()

    def data(self):
        print("name", self.name, end=", ")
        print("age", self.age, end=", ")
        print("game nic", self.nic)


class Liberty:
    def __init__(self):
        self.liberty = ["Можно банить", "разрешено добавлять сообщения ", "разрешено удалять пользователей"]

    def print_liberty(self):
        print("Возможности админа:", *self.liberty)


admin = Admin("Maga", 33, "Anime_girl")
admin.data()
admin.liberty.print_liberty()
