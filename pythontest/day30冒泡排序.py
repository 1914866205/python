"""
冒泡排序
"""


def bubble_sort(items, comp=lambda x, y: x > y):
    items = items[:]
    for i in range(len(items)-1):
        swapped = False
        for j in range(i, len(items)-1-i):
            if comp(items[j], items[j+1]):
                items[j], items[j+1] = items[j+1], items[j]
                swapped = True
            if not swapped:
                break
        return items


items = [5, 13, 54, 95, 3]


print(bubble_sort(items))
