def reverse(s):
    if(not s):
        return False
    l = []
    for i in s.split():
        l.append(i)
    result = ''
    for i in l[::-1]:
        result += (i + ' ')
    return result[:-1]

def leftRotate(s, k):
    if(not s or k <=-1 or k >= len(s)):
        return False
    result = ''
    result = s[k:]+s[:k]
    return result

if __name__ == '__main__':
    l = "I am a student."
    print(reverse(l))
    s = 'abcdefg'
    print(leftRotate(s,0))