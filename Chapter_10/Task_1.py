with open("info.txt", "r", encoding="utf-8") as f:
    info_file = f.readlines()

for i in info_file:
    print(i.strip().replace("люблю", "ненавижу"))

with open("info.txt", "r", encoding="utf-8") as f:
    info_str = f.read()

print(info_str.lstrip())

