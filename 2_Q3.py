#author: Ouyang Zhangjian
#date: 10/27/2016

x = raw_input("input your name:")

def head():
    print "********************"
    print "********************"


def waist():
    print "$$$$            $$$$"
    print "$$$$            $$$$"


def middle():
    print "====   %4s     ====" % (x)


def main():
    head()
    waist()
    middle()
    waist()
    head()

main()




