def maxProfit(l):
    if(not l or len(l)<2):
        return False
    min= l[0]
    curProfit = l[1]-min
    for i in range(1, len(l)):
        if(l[i]<min):
            min = l[i]
        if(l[i]-min>curProfit):
            curProfit = l[i]-min
    return curProfit

if __name__ == '__main__':
    l = [9,11,8,5,7,12,16,14]
    print(maxProfit(l))
