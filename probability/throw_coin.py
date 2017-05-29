# coding: UTF-8
# コインを９回投げて表が３回出る確率

from numpy.random import *

def throw():
    return [randint(2) for _ in range(9)]

def main():
    total = 100000
    data = [throw() for _ in range(total)]
    print(len(filter(lambda x: x == 0, map(convert ,data))) / float(total))

def convert(l):
    return float(sum(map(lambda x: 2 if x == 1 else -1 ,l)))


if __name__ == '__main__':
    main()