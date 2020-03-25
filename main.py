from request_data import get_data
from parse import parse_data

if __name__ == "__main__":
    goods = []
    for i in range(10):
        body = get_data(i)
        parse_data(body, goods)