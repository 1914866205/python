import random


def birthday(num):
    bir = {}
    for i in range(num):
        bir[i] = random.randint(1, 366)
    if len(set(bir.values())) == num:
        return True
    return False


countTrue=0
countFalse=0
for i in range(25, 366):
    if birthday(i):
        countTrue=countTrue+1
    else:
        countFalse=countFalse+1
print(countTrue)
print(countFalse)
