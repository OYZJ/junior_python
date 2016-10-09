# author: Ouyang Zhangjian
#date: 10/9/2016

a = input("enter your weight(kg): ")
b = input("enter your height(m): ")
BMI = a/(b**2)
print
print "Your BMI is: %0.2f" % BMI
if BMI < 19:
    print "You are slim!"
elif 19 <= BMI < 25:
    print "Your are health!"
elif 25 <= BMI < 28:
    print "You are a litle bit fat!"
else:
    print "You are too fat!!!"
