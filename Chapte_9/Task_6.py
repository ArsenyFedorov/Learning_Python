from random import choice


def lottery(user_list: list) -> list:
    lot_list = list()
    for _ in range(4):
        lot_list.append(choice(user_list))
    return lot_list


lottery_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "a", "b", "c", "d"]
win_ticket = ["a", 1, 3, "c"]

count = 0
flag = True
while flag:
    my_list = lottery(lottery_list)
    if win_ticket == my_list:
        print(count)
        flag = False
    count += 1


