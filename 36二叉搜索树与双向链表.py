class TreeNode(object):
    def __init__(self, n):
        self.val = n
        self.lchild = None
        self.rchild = None

def Convert(T):
    if(not T):
        return None
    maxInTree = ConvertNode(T, None)
    p = maxInTree
    while(p.lchild):
        p = p.lchild
    return p

def ConvertNode(T, plast):
    if(not T):
        return None
    if(T.lchild):
        plast = ConvertNode(T.lchild, plast)
    #如果某点左子树存在最大点，则将最大点的右指针指向该点
    #如果没有左子树，则最大点为该点父节点处产生的最大点，将它的右指针指向该点
    if(plast):
        plast.rchild = T
    T.lchild = plast
    plast = T
    if(T.rchild):
        plast = ConvertNode(T.rchild, plast)
    return plast

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
    p = Convert(pNode1)
    while(p):
        print(p.val)
        p = p.rchild