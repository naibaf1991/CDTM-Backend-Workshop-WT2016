import random as r

def tutorial1():
    s1 = "Fabian"
    s2 = "Kieferngarten"
    print s1 + " " + s2

def tutorial2():
    l1 = [i for i in range(1,101)]
    l2 = [i for i in range(1,101) if i != 50]
    print l2

class fabi(object):
    def __init__(self):
        self.name1 = "fabi"
        self.age = 25
        self.study = "MechEng"

    def ageing(self):
        self.age += 1

class maxi(fabi):
    def __init__(self, iq):
        fabi.__init__(self)
        self.iq = iq

    def getIQ(self):
        print self.iq -50
        return self.iq -50

def randomlist():
    l1 = [int(r.random()*10+1) for i in range(0,101)]
    return l1

def bubblesort(l1):
        

def main():
    tutorial2()
    depp = maxi(100)
    depp.getIQ()
    print randomlist()

if __name__ == '__main__':
    main()