class treeNode(object):
    def __init__(self, n):
        treeNode.val = n
        treeNode.lchild = None
        treeNode.rchild = None
        treeNode.father = None

def find_next(T):
    if( not T):
        return
    if(T.rchild):
        p = T.rchild
        while(p.lchild):
            p = p.lchild
        return p
    else:
        if(T.father and T.father.lchild == T):
            return T.father
        elif(T.father and T.father.rchild == T):
            p = T.father
            while(p.father and p.father.rchild == p):
                p = p.father
            if(p.father):
                return p.father
            else:
                return
        else:
            return


