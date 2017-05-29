# coding: UTF-8
# サイコロを４回振って３回１が出る確率
# NOT 関数型

import numpy
from numpy.random import *




def main():
    count = 0.0
    for _ in range(10000):
        if throw():
            count += 1.0
    print(count / 10000.0)
    

def throw():
    one_num = 0
    for _ in range(4):
        num = randint(1,7)
        if num == 1:
            one_num += 1
    if one_num == 3:
        return True
    else:
        return False
    
     

if __name__ == '__main__':
    main()
