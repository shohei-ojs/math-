import numpy as np
import matplotlib as plot

def f(x):
    return x**2

def d(a):
    h = 1e-8
    return (f(a + h) - f(a)) / h

def main():
    print(d(5))
    
    


if __name__ == '__main__':
    main()