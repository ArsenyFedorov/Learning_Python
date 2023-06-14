user_name = input("Ввидите имя:")

with open("user.txt", "w", encoding="utf-8") as f:
    f.write(f"Hello {user_name}")

