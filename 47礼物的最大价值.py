def maxValue(M, rows, cols):
    if(not M or rows <= 0 or cols <= 0):
        return False
    maxValues = [0]*cols
    for i in range(rows):
        for j in range(cols):
            left = 0
            up = 0
            if(i>0):
                up = maxValues[j]
            if(j>0):
                left = maxValues[j-1]
            maxInij = max(left, up) + M[i][j]
            maxValues[j] = maxInij
    return maxValues[-1]

if __name__ == '__main__':
    M = [[1,10,3,8],
         [12,2,9,6],
         [5,7,4,11],
         [3,7,16,5]]
    rows = len(M)
    cols = len(M[0])
    print(maxValue(M, rows, cols))