def circleMatrix(M):
    if(not M):
        return False
    rows = len(M)
    columns = len(M[0])
    if(rows == 0 or columns == 0):
        return False
    start = 0
    while(2 * start < rows and 2 * start < columns ):
        printCircle(M, rows, columns, start)
        start += 1

def printCircle(M, rows, columns, start):
    maxCol = columns-1-start
    maxRow = rows-1-start
    i = start
    while(i <= maxCol):
        print(M[start][i], end = ' ')
        i += 1
    if(maxRow > start):
        i = start+1
        while(i <= maxRow):
            print(M[i][maxCol], end = ' ')
            i += 1
    if(maxCol > start and maxRow > start):
        i = maxCol-1
        while(i >= start):
            print(M[maxRow][i], end = ' ')
            i -= 1
    if(maxRow - start > 1 and start < maxCol):
        i = maxRow-1
        while(i > start):
            print(M[i][start], end = ' ')
            i -= 1

if __name__ == '__main__':
    matrix = [[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12],
              [13, 14, 15, 16]]
    matrix2 = [[1], [2], [3], [4], [5]]
    matrix3 = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]
    circleMatrix(matrix)
    print('\n')
    circleMatrix(matrix2)
    print('\n')
    circleMatrix(matrix3)


