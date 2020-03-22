import functools
def compare(s1, s2):
    if(s1+s2 < s2+s1):
        return -1
    if(s1+s2 > s2 + s1):
        return 1
    if(s1+s2 == s2+s1):
        return 0

def leastCombine(l):
    if(not l):
        return False
    s = []
    for i in l:
        s.append(str(i))
    s.sort(key = functools.cmp_to_key(compare))
    result = ''
    for i in s:
        result += i
    return int(result)

if __name__ == '__main__':
    l = [3, 32, 321]
    print(leastCombine(l))
