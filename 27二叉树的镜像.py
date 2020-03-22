class TreeNode(object):
    def __init__(self, n):
        self.val = n
        self.lchild = None
        self.rchild = None

def mirror(T):
    if (not T):
        return
    if(not T.lchild and not T.rchild):
        return T
    tmp = T.rchild
    T.rchild = T.lchild
    T.lchild = tmp
    mirror(T.lchild)
    mirror(T.rchild)

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
    mirror(pNode1)
    print(pNode1.rchild.lchild.val)
