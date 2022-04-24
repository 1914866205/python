def multi(*num):
    result=1
    for i in num:
        result*=i
    return result


print(multi(1,2,3,4,5))
