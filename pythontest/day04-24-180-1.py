import random
items = ""
for i in range(65, 91):
    items += chr(i)
    items += chr(i + 32)
for i in range(48, 58):
    items += chr(i)
for i in range(10):
    for j in range(8):
        print(random.choice(items),end="")
    print("\n")

