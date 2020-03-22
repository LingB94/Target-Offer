def translate(s):
    dict = {'King':0, 'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'J':11, 'Q':12, 'K':13}
    l = []
    for i in s:
        l.append(dict[i])
    return l

def isContinuous(s):
    l = translate(s)
    if(not l or len(l)<5):
        return False
    ZeroNum, GapNum = 0, 0
    for i in l:
        if(i == 0):
            ZeroNum += 1
    s = sorted(l)
    for i in range(len(s)-1):
        if(s[i] == 0):
            continue
        elif(s[i] == s[i+1]):
            return False
        GapNum += (s[i+1]-s[i]-1)
    if(ZeroNum == GapNum):
        return True
    return False

if __name__ == '__main__':
    s = ['A','2','3','5','King']
    print(isContinuous(s))
