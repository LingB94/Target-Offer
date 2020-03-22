def inversePairs(l):
    if(not l):
        return False
    start = 0
    end = len(l)-1
    copy= [i for i in l]
    cnt = inversePairsCore(copy, start, end)
    return cnt

def inversePairsCore(copy, start, end):
    if(start == end):
        return 0
    middle = (start + end)//2
    p1, p2 = middle, end
    cnt = 0
    left = inversePairsCore(copy,start, middle)
    right = inversePairsCore(copy, middle+1, end)
    tmp = []
    while(p1 >= start and p2 >= middle+1):
        if(copy[p1] > copy[p2]):
            cnt += (p2-middle)
            tmp.append(copy[p1])
            p1 -= 1
        else:
            tmp.append(copy[p2])
            p2 -= 1
    while(p2>=middle+1):
        tmp.append(copy[p2])
        p2 -= 1
    while(p1>=start):
        tmp.append(copy[p1])
        p1 -= 1
    copy[start:end+1] = tmp[::-1]
    return cnt + left + right

if __name__ == '__main__':
    l = [7,5,6,4]
    print(inversePairs(l))
