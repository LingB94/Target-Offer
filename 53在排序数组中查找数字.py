def getOccurence(l, k):
    if(not l):
        return False
    firstK = getFirstK(l,k,0,len(l)-1)
    lastK = getLastK(l,k,0,len(l)-1)
    if(not firstK):
        return False
    else:
        return lastK - firstK + 1

def getFirstK(l, k, start, end):
    mid = (start+end)//2
    if(l[mid]==k):
        if(mid == 0 or l[mid-1] != k):
            return mid
        else:
            return getFirstK(l,k,start,mid-1)
    if(l[mid]>k):
        return getFirstK(l,k,start,mid-1)
    if(l[mid]<k):
        return getFirstK(l,k,mid+1,end)
    return None

def getLastK(l,k,start,end):
    mid = (start+end)//2
    if(l[mid]==k):
        if(mid == len(l)-1 or l[mid+1] != k):
            return mid
        else:
            return getLastK(l,k,mid+1,end)
    if(l[mid]>k):
        return getLastK(l,k,start,mid-1)
    if(l[mid]<k):
        return getLastK(l,k,mid+1,end)
    return None

if __name__ == '__main__':
    l = [1,2,3,3,3,3,4,5]
    print(getOccurence(l, 3))