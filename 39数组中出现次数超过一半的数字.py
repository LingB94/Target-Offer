def moreThanHalf(l):
    if(len(l) == 0):
        return False
    middle = len(l)>>1
    start = 0
    end = len(l)-1
    index = partition(l, start, end)
    while(index != middle):
        if(index > middle):
            end = index-1
            index = partition(l,start,end)
        if(index < middle):
            end = index+1
            index = partition(l,start,end)
    result = l[index]
    if(not checkRight(l, result)):
        return False
    return result

def partition(l, start, end):
    pivot = l[end]
    i = start-1
    #i记录当前索引以后比pivot大的第一个数数
    #遍历从start到end的数，如果都比pivot的小则i和j一直相等，相当于没交换，直到碰到第一个比pivot大的数
    #此时i指向比pivot小的最后一个数，j指向其后第一个比pivot大的数，交换彼此
    #遍历结束后i指向比pivot小的最后一个数，加1后与pivot交换
    for j in range(start, end):
        if(l[j] <= pivot):
            i += 1
            l[i], l[j] = l[j], l[i]
    l[i+1], l[end] = l[end], l[i+1]
    return i+1

def checkRight(l, result):
    cnt = 0
    for i in range(len(l)):
        if(l[i] == result):
            cnt += 1
    if(cnt * 2 <= len(l)):
        return False
    return True

def moreThanHalf2(l):
    if(len(l) == 0):
        return False
    result = l[0]
    cnt = 1
    for i in range(1, len(l)):
        if(cnt == 0):
            result = l[i]
            cnt = 1
        elif(l[i] == result):
            cnt += 1
        else:
            cnt -= 1
    if (not checkRight(l, result)):
        return False
    return result

if __name__ == '__main__':
    l = [1,2,3,2,2,2,5,4,2]
    print(moreThanHalf(l))
    print(moreThanHalf2(l))
    l2 = [1]
    print(moreThanHalf(l2))
    l3 = []
    print(moreThanHalf(l3))


