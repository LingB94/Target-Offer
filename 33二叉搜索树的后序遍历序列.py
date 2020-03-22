class TreeNode(object):
    def __init__(self, n):
        self.val = n
        self.lchild = None
        self.rchild = None

def verify(L):
    if(not L):
        return False
    p = L[-1]
    step1 = 0
    while(L[step1] < p and step1 < len(L)):
        step1 += 1
    for step2 in range(step1, len(L)):
        if(L[step2] < p):
            return False
    left = True
    if(step1 > 0):
        left = verify(L[:step1])
    right = True
    if(step1 < len(L)-1):
        right = verify(L[step1:len(L) - 1])
    return left and right

if __name__ == '__main__':
    array = [5, 7, 6, 9, 11, 10, 8]
    array2 = [4, 6, 7, 5]
    array3 = [1, 2, 3, 4, 5]
    array4 = [7, 4, 6, 5]
    print(verify(array))
    print(verify(array2))
    print(verify(array3))
    print(verify(array4))

