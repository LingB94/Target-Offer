class treeNode(object):
    def __init__(self, n):
        self.val = n
        self.lchild = None
        self.rchild = None

def constructTree(pre, inx):
    if(not pre or not inx):
        return None
    root = treeNode(pre[0])
    i = inx.index(pre[0])
    root.lchild = constructTree(pre[1:i+1], inx[:i])
    root.rchild = constructTree(pre[i+1:], inx[i+1:])
    return root

def pre_traversal(T):
    if(not T):
        return
    print(T.val)
    pre_traversal(T.lchild)
    pre_traversal(T.rchild)

def inx_traversal(T):
    if(not T):
        return
    inx_traversal(T.lchild)
    print(T.val)
    inx_traversal(T.rchild)

def post_traversal(T):
    if(not T):
        return
    post_traversal(T.lchild)
    post_traversal(T.rchild)
    print(T.val)

def level_traversal(T):
    if(not T):
        return
    queue = []
    queue.append(T)
    while(queue):
        node = queue[0]
        if(node.lchild):
            queue.append(node.lchild)
        if(node.rchild):
            queue.append(node.rchild)
        x = queue.pop(0)
        print(x.val)

if __name__ == '__main__':
    pre = [1,2,4,7,3,5,6,8]
    inx = [4,7,2,1,5,3,8,6]
    t = constructTree(pre, inx)
    level_traversal(t)