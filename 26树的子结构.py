from math import isclose
class TreeNode(object):
    def __init__(self, n):
        self.val = n
        self.lchild = None
        self.rchild = None

def findRoot(T1, T2):
    result = False
    if(T1 and T2):
        if(isclose(T1.val, T2.val)):
            result = judgeSub(T1, T2)
        if(not result):
            result = findRoot(T1.lchild, T2)
        if(not result):
            result = findRoot(T1.rchild, T2)
    return result

def judgeSub(T1, T2):
    if(not T2):
        return True
    if(not T1):
        return False
    if(not isclose(T1.val, T2.val)):
        return False
    return judgeSub(T1.lchild, T2.lchild) and judgeSub(T1.rchild, T2.rchild)

if __name__ == '__main__':
    pRoot1 = TreeNode(8)
    pRoot2 = TreeNode(8)
    pRoot3 = TreeNode(7)
    pRoot4 = TreeNode(9)
    pRoot5 = TreeNode(2)
    pRoot6 = TreeNode(4)
    pRoot7 = TreeNode(7)
    pRoot1.left = pRoot2
    pRoot1.right = pRoot3
    pRoot2.left = pRoot4
    pRoot2.right = pRoot5
    pRoot5.left = pRoot6
    pRoot5.right = pRoot7

    pRoot8 = TreeNode(8)
    pRoot9 = TreeNode(9)
    pRoot10 = TreeNode(2)
    pRoot8.left = pRoot9
    pRoot8.right = pRoot10
    print(findRoot(pRoot1, pRoot8))
