#author: Ouyang Zhangjian
#date: 10/27/2016

n = input("input a number:")
sum = 1

def fact(n):
    if n == 0:
        return 1
    return n * fact(n - 1)

for i in range(1,n+1):
    sum = sum + float(i)/float(fact(i))

print sum


