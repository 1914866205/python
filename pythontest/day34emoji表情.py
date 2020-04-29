"""
使用Pyhton实现emoji表情
pip3 install emoji
"""
import emoji

# 默认的表情可以直接通过表情的字符实现
# https://www.unicode.org/emoji/charts/emoji-list.html
# Python is
print(emoji.emojize('Python is :thumbs_up:'))
# 有些帖上个月的表情需要制定 use_aliases=True参数才可以实现
print(emoji.emojize('Sleeping is :zzz:', use_aliases=True))
# 可以单词形式
print(emoji.emojize('你是猪么？ :rolling_on_the_floor)laughing:'))
# 也可以使用unicode格式
print(emoji.emojize('\U0001F32D'), emoji.emojize('\U0001F354'),
      emoji.emojize('\U0001F35F'), emoji.emojize('\U0001F355'),
      emoji.emojize('\U0001F35F'), emoji.emojize('\U0001F355')
      )
print(emoji.emojize('\U0001F33A'), emoji.emojize('\U0001F33A'),
      emoji.emojize('\U0001F33A'), emoji.emojize('\U0001F355'),
      emoji.emojize('\U0001F33A'), emoji.emojize('\U0001F355')
      )
print(emoji.emojize('\U0001F497'), emoji.emojize('\U0001F496'),
      emoji.emojize('\U0001F495'), emoji.emojize('\U0001F497'),
      emoji.emojize('\U0001F496'), emoji.emojize('\U0001F495')
      )
