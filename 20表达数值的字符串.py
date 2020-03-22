def isNumeric(s):
    if(not s):
        return False
    pointCnt, eCnt = 0, 0
    pointPos, ePos = None, None
    for i, num in enumerate(s):
        if(num == '.'):
            pointPos = i
            pointCnt += 1
        if(num == 'e' or num == 'E'):
            ePos = i
            eCnt += 1
    if(pointCnt > 1 or eCnt > 1):
        return False
    elif(ePos and pointPos and ePos < pointPos):
        return False
    elif(ePos == len(s) - 1):
        return False
    sLower = [x.lower() for x in s]
    numeric = False
    if(pointCnt and eCnt):
        numeric = judgeInteger(sLower[:pointPos])
        numeric = judgeUnsignInt(sLower[pointPos+1:ePos]) and numeric
        numeric = judgeInteger(sLower[ePos+1:]) and numeric
    elif(pointCnt and (eCnt == 0)):
        numeric = judgeInteger(sLower[:pointPos])
        numeric = judgeUnsignInt(sLower[pointPos+1:]) and numeric
    elif((pointCnt == 0) and eCnt):
        numeric = judgeInteger(sLower[:ePos]) and judgeInteger(sLower[ePos+1:])
    else:
        numeric = judgeInteger(sLower)
    return numeric

def judgeInteger(s):
    Allow = {'+','-','0','1','2','3','4','5','6','7','8','9'}
    for i in range(len(s)):
        if(s[i] not in Allow):
            return False
        if(s[i] in '+-' and i != 0):
            return False
    return True

def judgeUnsignInt(s):
    Allow = {'0','1','2','3','4','5','6','7','8','9'}
    for i in range(len(s)):
        if(s[i] not in Allow):
            return False
    return True

if __name__ == '__main__':
    test = '12e+5.4'
    print(isNumeric(test))