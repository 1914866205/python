class Goods(object):

    def __init__(self, price=0.0, title='', page=''):
        self.price = float(price)
        self.title = title
        self.page = 'https:' + page


    def __repr__(self):
        return self.title

    def __str__(self):
        return self.title
