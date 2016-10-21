# author: Ouyang Zhangjian 5140309006
# date: 10/13/2016

from math import *
x = input("input the independent variable:")
def f(x):
    if x < 0:
        print (x+1)**2+2*x+1/x
    else:
        print sqrt(x)
f(x)
