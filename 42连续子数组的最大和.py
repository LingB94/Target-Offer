def greatestSum(l):
    assert l, 'l is empty!'
    #tmpSum设为0，
    tmpSum, maxSum = 0, l[0]
    for i in range(0,len(l)):
        tmpSum += l[i]
        if(tmpSum >= maxSum):
            maxSum = tmpSum
        if(tmpSum <= 0):
            tmpSum = 0
    return maxSum

if __name__ == '__main__':
    l = [1,-2,3,10,-4,7,2,-5]
    print(greatestSum(l))
    l2 = [-3,-1,1,-2]
    print(greatestSum(l2))
    l3 = [-3,-2,-4,-5]
    print(greatestSum(l3))
    l1 = []
    print(greatestSum(l1))
