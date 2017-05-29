# coding: UTF-8
# 数字の書かれたカードを引いた時の期待値
# ①：カードの数字＊１００円
# ②：５が出た場合１０００円

from numpy.random import *


CARDS = [1,2,2,3,3,3,4,4,4,4,5,5,5,5,5]
TOTAL = 100000

def draw():
    return choice(CARDS)

def mean(l):
    return sum(l) /TOTAL

def main():
    a = mean([draw() * 100 for _ in range(TOTAL)])
    b = mean([1000 if draw() == 5 else 0 for _ in range(TOTAL)])
    print('1さんは%s円くらい' % a)
    print('2さんは%s円くらい' % b)

if __name__ == '__main__':
    main()