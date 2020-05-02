"""
使用 @property装类属性
"""


class Book(object):
    def __init__(self, name, sale):
        self._name = name
        self._sale = sale

    @property
    def name(self):
        return self._name


a_book = Book('magic_book', 100000)
print(a_book.name)
