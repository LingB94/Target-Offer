def findNum(Matrix, num):
    rows = len(Matrix)
    cols = len(Matrix[0])
    row, col = rows - 1, 0
    while(row >= 0 and col < cols):
       if(Matrix[row][col] == num):
           return True
       elif(Matrix[row][col] < num):
           col += 1
       else:
           row -= 1
    return False

if __name__ == '__main__':
    M = [ [1,2,8,9],
          [2,4,9,12],
          [4,7,10,13],
          [6,8,11,15]]
    print(findNum(M, 7))