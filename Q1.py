# author: Ouyang Zhangjian 5140309006
# date: 10/13/2016

num = raw_input ("enter 4 digitals:")
i = 0
a = ()
while i < 4:
    print (eval(num[i])+9)%10,
    i = i + 1