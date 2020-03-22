def countNum(rows, cols, k):
    if (rows < 1 or cols < 1 or k < 0):
        return False
    visited = [[0 for i in range(cols)] for j in range(rows)]
    cnt = countNumCore(rows,cols,0,0,visited,k)
    return cnt

def countNumCore(rows,cols,row,col,visited,k):
    cnt = 0
    if(checkNum(rows,cols,row,col,k,visited)):
        visited[row][col] = True
        cnt = 1 + countNumCore(rows,cols,row+1,col,visited,k) +\
                countNumCore(rows,cols,row,col+1,visited,k) +\
                countNumCore(rows,cols,row-1,col,visited,k) +\
                countNumCore(rows,cols,row,col-1,visited,k)
    return cnt

def checkNum(rows, cols,row,col,k,visited):
    if(row >= 0 and row < rows and col >= 0 and col < cols and not visited[row][col]):
        # print("check:",row,col)
        if((getdigitSum(row)+getdigitSum(col))<=k):
            return True
    return False

def getdigitSum(x):
    sum = 0
    # print("number:",x)
    while(x > 0):
        # print(x)
        sum += (x%10)
        x = x//10
    return sum

if __name__ == '__main__':
    print(countNum(30, 30, 3))
