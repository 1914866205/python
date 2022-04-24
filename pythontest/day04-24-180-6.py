import jieba

excludes = {"什么", "一个", "我们", "那里", "如今", "你们", "说道", "知道", "起来", "姑娘", "这里", "出来", "他们", "众人", "自己", "一面", "只见", "怎么",
            "两个", "不是", "不知", "这个", "听见", "这样", "没有", "进来", "告诉", "东西", "咱们","就是", "回来", "大家","只是"}
txt = open("D:\CompcuteApplication\projectTest\pythonTest\\res\\txt\红楼梦.txt", "r", encoding="utf-8").read()
words = jieba.lcut(txt)
counts = {}
for word in words:
    if len(word) == 1:
        continue
    else:
        counts[word] = counts.get(word, 0) + 1
for word in excludes:
    del (counts[word])
items = list(counts.items())
items.sort(key=lambda x: x[1], reverse=True)
for i in range(15):
    word, count = items[i]
    print("{0:<10}{1:>5}".format(word, count))
