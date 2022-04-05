for i in range(11):
    for j in range(11):
        if (i % 5 == 0) & (j % 5 == 0):
            if j == 10:
                print("+")
            else:
                print("+", end="")
        elif i % 5 == 0:
            if j == 10:
                continue
            else:
                print("——", end="")
        elif j % 5 == 0:
            if j == 10:
                print("|")
            else:
                print("|", end="")
        else:
            print("  ", end="")
