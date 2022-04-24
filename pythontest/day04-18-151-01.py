# for i in range(11):
#     for j in range(11):
#         if (i % 5 == 0) & (j % 5 == 0):
#             if j == 10:
#                 print("+") #换行
#             else:
#                 print("+", end="") #不换行
#         elif i % 5 == 0:
#             if j == 10:
#                 continue
#             else:
#                 print("— ", end="")
#         elif j % 5 == 0:
#             if j == 10:
#                 print("|")
#             else:
#                 print("|", end="")
#         else:
#             print("  ", end="")

def tian(n):
    for i in range(5*n+1):
        for j in range(5*n+1):
            if (i % 5 == 0) & (j % 5 == 0):
                if j == 5*n:
                    print("+")
                else:
                    print("+", end="")
            elif i % 5 == 0:
                if j == 5*n:
                    continue
                else:
                    print("— ", end="")
            elif j % 5 == 0:
                if j == 5*n:
                    print("|")
                else:
                    print("|", end="")
            else:
                print("  ", end="")

tian(4)