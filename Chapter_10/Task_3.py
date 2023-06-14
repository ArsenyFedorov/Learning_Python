with open("guest.txt", "a", encoding="utf-8") as f:
    while True:
        user_name = input("Ввидите имя :")
        if user_name == "":
            break
        f.write(f"{user_name}\n")
