class TreeNode(object):
    def __init__(self, n):
        self.val = n
        self.lchild = None
        self.rchild = None

def isSymmetrical(T):
    return selfSymmetrical(T, T)

def selfSymmetrical(T1, T2):
    if(not T1 and not T2):
        return True
    if(not T1 or not T2):
        return False
    if(T1.val != T2.val):
        return False
    return selfSymmetrical(T1.lchild, T2.rchild) and selfSymmetrical(T1.rchild, T2.lchild)

if __name__ == '__main__':
    pNode1 = TreeNode(8)
    pNode2 = TreeNode(6)
    pNode3 = TreeNode(10)
    pNode4 = TreeNode(5)
    pNode5 = TreeNode(7)
    pNode6 = TreeNode(9)
    pNode7 = TreeNode(11)

    pNode1.lchild = pNode2
    pNode1.rchild = pNode3
    pNode2.lchild = pNode4
    pNode2.rchild = pNode5
    pNode3.lchild = pNode6
    pNode3.rchild = pNode7
    print(isSymmetrical(pNode1))