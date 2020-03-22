import heapq

def leastK(l, n, k):
    if(not l or n <= 0 or k <= 0 or n < k):
        return False
    start = 0
    end = n-1
    index = partition(l, start, end)
    while(index != k):
        if(index < k):
            start = index+1
            index = partition(l, start, end)
        if(index > k):
            end = index-1
            index = partition(l, start, end)
    for i in range(k):
        print(l[i])

def partition(l, start, end):
    pivot = l[end]
    i = start-1
    for j in range(start, end):
        if(l[j] <= pivot):
            i += 1
            l[i], l[j] = l[j], l[i]
    l[i+1], l[end] = l[end], l[i+1]
    return i+1

def leastK2(l, n, k):
    if (not l or n <= 0 or k <= 0 or n < k):
        return False
    h = []
    for num in l[0:k]:
        num = (-1)*num
        heapq.heappush(h, num)
    for num in l[k:]:
        num = (-1)*num
        maxInHeap = h[0]
        if(num > maxInHeap):
            heapq.heapreplace(h, num)
    for i in h:
        print((-1)*i)

if __name__ == '__main__':
    l = [4,5,1,6,2,7,3,8]
    leastK(l, 8, 4)
    leastK2(l, 8, 4)