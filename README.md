# Target-Offer
剑指offer第二版-python3实现

[2:单例模式singleton](https://github.com/LingB94/Target-Offer/blob/master/2%E5%8D%95%E4%BE%8B%E6%A8%A1%E5%BC%8F.py)
单例模式即使某个类只能访问一个唯一的对象（例如一个班只能有一个班主任）。python中的构造方法分为创建对象和初始化对象两步，前者使用__new__，后者使用__init__。new方法必须有一个参数clf表示要实例化的类（如班主任），同时要返回一个对象。在singleton类中定义一个用于存放类名的set，如果创建对象时这个set中没有“班主任”类，则正常创建，否则返回“班主任”。这样在使用班主任类创建两个变量时，因为new在init之前执行，这两个变量只能指向同一个对象。

[另一种解决方法](https://github.com/LingB94/Target-Offer/blob/master/2(1)%E5%8D%95%E4%BE%8B%E6%A8%A1%E5%BC%8F.py)
利用装饰器。装饰器是返回值为函数的函数，将它放在类定义的前面，我们就会在使用某个类（班主任）时自动将该类作为装饰器的输入参数。可以在装饰器函数内部定义一个用于存放类名的set，让装饰器返回的函数仅返回在set中“班主任”类。两种单例模式的方法都用到了python中的set，set即集合，其中不允许重复。

[4:二维数组中的查找](https://github.com/LingB94/Target-Offer/blob/master/4%E4%BA%8C%E7%BB%B4%E6%95%B0%E7%BB%84%E4%B8%AD%E7%9A%84%E6%9F%A5%E6%89%BE.py)
矩阵从上到下递增，从左到右递增。从矩阵的左下角开始找起。左下角的元素必然比它所在列的所有元素都大，比它所在行的所有元素都小。如果左下角的元素比目标元素大，则排除最后一行，如果比目标元素小，则排除第一列。

[5:替换空格](https://github.com/LingB94/Target-Offer/blob/master/5%E6%9B%BF%E6%8D%A2%E7%A9%BA%E6%A0%BC.py)
用一个空列表从头开始记录

[6:从尾到头打印链表](https://github.com/LingB94/Target-Offer/blob/master/6%E4%BB%8E%E5%B0%BE%E5%88%B0%E5%A4%B4%E6%89%93%E5%8D%B0%E9%93%BE%E8%A1%A8.py)
利用栈实现循环的方法，也可以用递归的方法

[7:重建二叉树](https://github.com/LingB94/Target-Offer/blob/master/7%E9%87%8D%E5%BB%BA%E4%BA%8C%E5%8F%89%E6%A0%91.py)
根据前序遍历和中序遍历确定树的结构。以前序遍历的第一个节点为根，在中序遍历中找到该点的位置（记为i）。根的左子树所有节点为前序遍历中的1到i，中序遍历中的0到i-1；根的右子树所有节点为前序遍历中的i+1到-1，中序遍历中的i+1到-1。递归构造左右子树

[8:二叉树的下一个节点](https://github.com/LingB94/Target-Offer/blob/master/8%E4%BA%8C%E5%8F%89%E6%A0%91%E7%9A%84%E4%B8%8B%E4%B8%80%E4%B8%AA%E8%8A%82%E7%82%B9.py)
若该点有右子树，则下一个节点为该点右孩子的最左后代；若该点无右子树且为其父节点的左孩子，则下一个节点为其父节点；若该点无右子树且为其父节点的右孩子，则不断上溯，直至找到某个点为其父节点的左孩子，下一个节点为这个父节点。如果到最后也找不到这样的点，则该点为最后一个点。

[9:用两个栈实现队列](https://github.com/LingB94/Target-Offer/blob/master/9%E7%94%A8%E4%B8%A4%E4%B8%AA%E6%A0%88%E5%AE%9E%E7%8E%B0%E9%98%9F%E5%88%97.py)
第一个栈仅用于压入新元素，第二个栈仅用于删除旧元素。当第二个栈不为空时，删除操作即删除第二个栈的栈顶；当第二个栈为空时，删除操作即将第一个栈中的所有元素压入第二个栈，然后从第二个栈删除

[10:斐波那契数列](https://github.com/LingB94/Target-Offer/blob/master/10%E6%96%90%E6%B3%A2%E9%82%A3%E5%A5%91%E6%95%B0%E5%88%97.py)
两种方法，递归或循环。
