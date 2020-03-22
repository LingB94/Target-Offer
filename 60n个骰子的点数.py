def cntProb(num):
    if(num <= 0):
        return False
    Prob = [[], []]
    diceMax = 6
    Prob[0] = [0]*(diceMax*num+1)
    flag = 0
    for i in range(1,diceMax+1):
        Prob[flag][i] = 1
    for dice in range(2, num+1):
        Prob[1-flag] = [0]*(diceMax*num+1)
        for curSum in range(dice, dice*diceMax+1):
            i = 1
            while(i<=diceMax and i<curSum):
                Prob[1-flag][curSum] += Prob[flag][curSum-i]
                i += 1
        flag = 1-flag
    total = pow(diceMax, num)
    for i in range(num, diceMax*num+1):
        ratio = Prob[flag][i]/float(total)
        print("SUM{}:{}".format(i, ratio) )

cntProb(6)