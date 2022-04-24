str = input("请输入一串字母：")
counts = {}
print(str)
for word in str:
    counts[word] = counts.get(word, 0) + 1
items = list(counts.items())
items.sort(key=lambda x: x[1], reverse=True)
for i in items:
    print(i)
