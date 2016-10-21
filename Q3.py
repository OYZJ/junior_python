# author: Ouyang Zhangjian 5140309006
# date: 10/13/2016

x = input("input the amount of the cent(8~100):")
if x <= 8:
    print "error"
elif x >= 100:
    print "error"
else:
    a = int((x - 8) / 5) + 1 # the number of 5 cents
    while a > 0 :
        b = int((x - 3 - 5 * a) / 2)+1 # the number of 2 cents
        c = int((x - 5 * a - 2 * b - 1)) +1 # the number of 1 cent
        print "5cents:",a, "2cents:", b, "1cent:", c
        while b > 1:
            c = c+2
            print "5cents:",a, "2cents:", b-1, "1cent:", c
            b = b-1
        a = a-1
