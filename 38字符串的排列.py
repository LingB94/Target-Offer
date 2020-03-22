import itertools
def permutation(s):
    if(not s):
        return None
    if(len(s) == 1):
        return list(s)
    l = list(s)
    l.sort()
    result = []
    for i in range(len(l)):
        if(i > 0 and l[i] == l[i-1]):
            continue
        part2 = permutation(''.join(l[:i]) +''.join(l[i+1:]))
        for j in part2:
            result.append(l[i]+j)
    return result

def permutation2(s):
    result = [''.join(x) for x in itertools.permutations(s, len(s))]
    return list(result)
if __name__ == '__main__':
    s = 'abc'
    result = permutation(s)
    for i in result:
        print(i)
    result = permutation2(s)
    for i in result:
        print(i)

