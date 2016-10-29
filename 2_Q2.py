#author: Ouyang Zhangjian
#date:10/27/2016

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
n = input("input a number(<=7):")

j = 0
for i in range(1, n+1):
    print alpha[j:j+n-i+1]
    j = j+n-i+1