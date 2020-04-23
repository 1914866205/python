"""
冒泡排序
"""


def bubble_sort(items, comp=lambda x, y: x > y):
    items = items[:]
    for i in range(len(items)):
        swapped = False
        for j in range(len(items)-1-i):
            if comp(items[j], items[j+1]):
                items[j], items[j+1] = items[j+1], items[j]
                swapped = True
        if not swapped:
            break
    return items


items = [5, 13, 54, 95, 3]


print(bubble_sort(items))


# def bubble_sort(items, comp=lambda x, y: x > y):
#     items = items[:]
#     for i in range(len(items) - 1):
#         swapped = False
#         for j in range(i, len(items) - i - 1):
#             if comp(items[j], items[j + 1]):
#                 items[j], items[j + 1] = items[j + 1], items[j]
#                 swapped = True
#             if not swapped:
#                 break
#         return items


# # if __name__ == "__main__":
# items = [58, 28, 18, 88, 8]
# print(bubble_sort(items))
