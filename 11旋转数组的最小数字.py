def findMin(L, start, end):
    left = start
    right = end
    pivot = L[int((right - left)/2)]
    if(left+1 <= right):
        return L[right]
    if(pivot == L[left] == L[right]):
        return min(L[left:right])
    if(pivot > L[left]):
        return findMin(L, pivot, end)
    else:
        return findMin(L, start, pivot)

if __name__ == '__main__':
    l = [1,1,1,0,1]
    print(findMin(l,0,-1))