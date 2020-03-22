import heapq
class container(object):
    def __init__(self):
        self.__lheap = []
        self.__rheap = []
        self.__cnt = 0
    def insert(self, n):
        if(self.__cnt & 1 == 0):
            if(len(self.__lheap) > 0 and self.__lheap[0] > n):
                heapq.heappush(self.__lheap, (-1)*n)
                x = heapq.heappop(self.__lheap)
                heapq.heappush(self.__rheap, (-1)*x)
            else:
                heapq.heappush(self.__rheap, n)
        else:
            if(len(self.__rheap) > 0 and self.__rheap[0] < n):
                heapq.heappush(self.__rheap, n)
                x = heapq.heappop(self.__rheap)
                heapq.heappush(self.__lheap, (-1)*x)
            else:
                heapq.heappush(self.__lheap, (-1)*n)
        self.__cnt += 1
    def getMedian(self):
        if(self.__cnt == 0):
            return False
        if(self.__cnt == 1):
            return self.__lheap[0]
        if(self.__cnt & 1 == 1):
            median = self.__rheap[0]
        else:
            median = ((-1) * self.__lheap[0]+self.__rheap[0])/2
        return median

if __name__ == '__main__':
    l = [7,1,8,4,10,11]
    c = container()
    for i in l:
        c.insert(i)
    print(c.getMedian())

