def longestSubstring(s):
    if(not s):
        return False
    length = len(s)
    lastPos = [-1]*26
    curLength, maxLength = 0, 0
    for i in range(length):
        prevIndex = lastPos[ord(s[i]) - ord('a')]
        if(prevIndex<0 or (i-prevIndex) > curLength):
            curLength += 1
        else:
            if(curLength>maxLength):
                maxLength = curLength
            curLength = i-prevIndex
        lastPos[ord(s[i]) - ord('a')] = i
    if(curLength > maxLength):
        maxLength = curLength
    return maxLength

if __name__ == '__main__':
    l = 'arabcacfr'
    print(longestSubstring(l))