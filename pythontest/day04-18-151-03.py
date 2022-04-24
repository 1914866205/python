def isNum(str):
    if(type(str) == int or type(str) == float or type(str) == complex ):
        return True
    return False

print(isNum(1))
print(isNum(1.5))
print(isNum(complex(1,5)))
print(isNum("strs"))
