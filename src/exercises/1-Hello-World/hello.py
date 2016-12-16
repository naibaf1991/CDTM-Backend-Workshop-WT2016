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
    l1 = [int(r.random()*100+1) for i in range(0,101)]
    return l1

def bubblesort(l1):
    n = len(l1)
    for i in range(n,0,-1):
        for k in range(0, n-1):
            if l1[k] > l1[k+1]:
                #l1[k:k+2] = l1[k:k+2:-1]
                temp = l1[k]
                l1[k] = l1[k+1]
                l1[k+1] = temp
    return l1

def main():
    print randomlist()
    print bubblesort(randomlist())

if __name__ == '__main__':
    main()