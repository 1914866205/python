def isRepeat(items):
    if len(set(items))!=len(items):
        return True
    return False



items = ["7", "65", "7", "32", "9"]
print(isRepeat(items))
items2 = ["17", "65", "7", "32", "9"]
print(isRepeat(items2))
