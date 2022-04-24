def isRepeat(items):
    for i in range(len(items)):
        for j in range(len(items)):
            if items[i] == items[j] and i != j:
                return True
    return False


items = ["7", "65", "7", "32", "9"]
print(isRepeat(items))
items2 = ["17", "65", "7", "32", "9"]
print(isRepeat(items2))
