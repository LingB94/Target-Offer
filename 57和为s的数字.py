def SumForS(l, s):
    if(not l):
        return False
    p1, p2 = 0, len(l)-1
    while(p1<=p2):
        if(l[p1]+l[p2]<s):
            p1 += 1
        if(l[p1]+l[p2]>s):
            p2 -= 1
        if(l[p1]+l[p2]==s):
            return l[p1],l[p2]
    return False

def findContinuousSum(s):
    start, end = 1,2
    while(start <= (s+1)/2):
        if(continuousSum(start, end)<s):
            end += 1
        elif(continuousSum(start, end)>s):
            start += 1
        else:
            for i in range(start, end+1):
                print(i, end= ' ')
            print('')
            end += 1

def continuousSum(start, end):
    sum = 0
    for i in range(start, end+1):
        sum += i
    return sum

if __name__ == '__main__':
    l = [1,2,4,7,11,15]
    print(SumForS(l, 15))
    s = 15
    findContinuousSum(s)