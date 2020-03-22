def findPath(M, rows, cols, path):
    if(not M or rows < 1 or cols < 1 or not path):
        return False
    visited = [[0 for i in range(cols)] for j in range(rows)]
    current = 0
    for row in range(rows):
        for col in range(cols):
            if(findPathCore(M, rows, cols, row, col, visited, path, current)):
                return True
    return False

def findPathCore(M,rows,cols,row,col,visited, path, current):
    flag = False
    if(current == len(path)):
        flag = True
    if(row < rows and row >= 0 and col < cols and col >= 0 and not visited[row][col] and M[row][col] == path[current]):
        current += 1
        visited[row][col] = True
        flag = findPathCore(M,rows,cols,row+1,col,visited, path, current) or \
                findPathCore(M,rows,cols,row,col+1,visited,path,current) or \
                findPathCore(M,rows,cols,row-1,col,visited,path,current) or \
                findPathCore(M,rows,cols,row,col-1,visited,path,current)
        if(flag==False):
            current -= 1
            visited[row][col] = False
    return flag

if __name__ == '__main__':
    M1 = [['a','b','t','g'],
          ['c','f','c','s'],
          ['j','d','e','h']]
    m1,n1 = 3,4
    print(findPath(M1,m1,n1,'bfce'))



