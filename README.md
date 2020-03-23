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

[11:旋转数组的最小数字](https://github.com/LingB94/Target-Offer/blob/master/11%E6%97%8B%E8%BD%AC%E6%95%B0%E7%BB%84%E7%9A%84%E6%9C%80%E5%B0%8F%E6%95%B0%E5%AD%97.py)
类似于二分查找，若数组中间元素大于第一个元素，则最小数字在中间元素后；若中间元素小于第一个元素，则则最小数字在中间元素前；若第一个元素、中间元素和最后一个元素相等，则只能顺序查找。此题有一个小bug，没有考虑旋转0个数字，即原递增数组不变的情况，这种情况只要在最开始的时候加一个判断即可。

[12:矩阵中的路径](https://github.com/LingB94/Target-Offer/blob/master/12%E7%9F%A9%E9%98%B5%E4%B8%AD%E7%9A%84%E8%B7%AF%E5%BE%84.py)
回溯法，定义用于记录某元素是否被访问过的矩阵visited，记录当前符合要求路径长度的变量current，每次从一个点开始，访问其周围的四个点来确定是否符合条件，不符合则回退current与visited，递归进行。

[13:机器人的运动范围](https://github.com/LingB94/Target-Offer/blob/master/13%E6%9C%BA%E5%99%A8%E4%BA%BA%E7%9A%84%E8%BF%90%E5%8A%A8%E8%8C%83%E5%9B%B4.py)
回溯法，从（0,0）开始，每次访问到符合条件的点，再访问该点四周的点

[14:剪绳子](https://github.com/LingB94/Target-Offer/blob/master/14%E5%89%AA%E7%BB%B3%E5%AD%90.py)
可以用从下到上的递归，定义一个列表记录长度为i的绳子剪完后所得的乘积。也可以用贪心算法，探索规律，当n>=5时，2(n-2),3(n-3)均大于n，表明如果剪出长度大于5的绳子，不如将其剪成长度为2或3的绳子。用贪心算法先剪出尽可能多的长度为3的绳子段，但如果剪完后只剩下一段长度为1的绳子时，应少剪一段长度为3的绳子，因为这样剩下的3+1=4的绳子可以剪成两段长度为2的绳子，乘积2*2>3*1。

[15:二进制中1的个数](https://github.com/LingB94/Target-Offer/blob/master/15%E4%BA%8C%E8%BF%9B%E5%88%B6%E4%B8%AD1%E7%9A%84%E4%B8%AA%E6%95%B0.py)
1个整数与它减去1后的数做位与运算，相当于将它最右边的1变成0。如果这个整数为负数，先将其与0xffffffff做与运算来获得它的补码，然后在完成前面的操作。做了几次操作其二进制中就有几个1

[16:数值的整数次方](https://github.com/LingB94/Target-Offer/blob/master/16%E6%95%B0%E5%80%BC%E7%9A%84%E6%95%B4%E6%95%B0%E6%AC%A1%E6%96%B9.py)
第一种方法分情况考虑，指数为整数、负数和0。第二种方法采用递归，求a的b次方可以变为a的b/2次方乘以a的b/2次方，如果b为奇数则还需再乘一个a。这里忘了写指数为0的判断。b/2可以用b>>1表示；任意一个数与1做位与运算，如果结果为1则该数为奇数。

[17:打印1到最大的n位数](https://github.com/LingB94/Target-Offer/blob/master/17%E6%89%93%E5%8D%B0%E4%BB%8E1%E5%88%B0%E6%9C%80%E5%A4%A7%E7%9A%84n%E4%BD%8D%E6%95%B0.py)
方法一：模拟数字的进位，第n位数字产生进位为循环的终止条件。数字的每一位存到一个列表中，每次在最后一位加1，根据是否进位计算前面的各位数。方法二：递归地全排列，对n位数上的数字用0到9填充，当填充到最后1位时打印。

[18:删除链表的节点](https://github.com/LingB94/Target-Offer/blob/master/18%E5%88%A0%E9%99%A4%E9%93%BE%E8%A1%A8%E7%9A%84%E8%8A%82%E7%82%B9.py)
计要删除的节点为i，其后继节点为j，将j的内容复制到i，i连接j的后继节点，在删除j。这样不用从头遍历找到i的前缀节点，时间复杂度为O(N)。如果i没有后继节点，则扔要从头遍历找到i的前缀节点。平均下来时间复杂度扔为O(N)

[19:正则表达式匹配](https://github.com/LingB94/Target-Offer/blob/master/19%E6%AD%A3%E5%88%99%E8%A1%A8%E8%BE%BE%E5%BC%8F%E5%8C%B9%E9%85%8D.py)
模式串与字符串匹配，可以递归地检查字符串首位与模式串开始的1或2位是否匹配。只有两种情况会匹配，第一种：与模式串开头的2位匹配，即模式串为'x*'的形式；第二种：与模式串开头的1位匹配，即模式串首位与字符串首位相等或模式串首位为'.'。在第一种情况下，又分为x为'.'或x等于字符串首位，以及x不等于'.'和字符串首位两种情况。对这些情况将模式串和字符串匹配的部分去掉后继续匹配

[20:表达数值的字符串](https://github.com/LingB94/Target-Offer/blob/master/20%E8%A1%A8%E8%BE%BE%E6%95%B0%E5%80%BC%E7%9A%84%E5%AD%97%E7%AC%A6%E4%B8%B2.py)
字符串必须符合[带符号的整数].[不带符号的整数]e/E[带符号的整数]这种形式。首先找到字符串中的小数点和E/e的位置，判断其合法性，小数点必须在E前面，E不能为最后一位，小数点和E都最多只能有一个。判断结束后根据小数点和E的情况分别判断

[21:调整数组顺序使奇数位于偶数前](https://github.com/LingB94/Target-Offer/blob/master/21%E8%B0%83%E6%95%B4%E6%95%B0%E7%BB%84%E9%A1%BA%E5%BA%8F%E4%BD%BF%E5%A5%87%E6%95%B0%E4%BD%8D%E4%BA%8E%E5%81%B6%E6%95%B0%E5%89%8D%E9%9D%A2.py)
设start从头遍历到尾，end从尾遍历到头，同时开始遍历，循环终止条件为start与end碰面。若start遇到偶数，end遇到了奇数，则交换。

[22:链表中倒数第k个节点](https://github.com/LingB94/Target-Offer/blob/master/22%E9%93%BE%E8%A1%A8%E4%B8%AD%E5%80%92%E6%95%B0%E7%AC%ACk%E4%B8%AA%E8%8A%82%E7%82%B9.py)
设两个指针，第一个比第二个先走k步，第一个到链表尾即第二个到倒数第k个点。注意要考虑k小于等于0，k大于链表长度，链表为空的情况

[23:链表中环的入口](https://github.com/LingB94/Target-Offer/blob/master/23%E9%93%BE%E8%A1%A8%E4%B8%AD%E7%8E%AF%E7%9A%84%E5%85%A5%E5%8F%A3.py)
确定是否有环：设快慢两个指针，快指针比慢指针每次多走两步，两指针相遇则有环。确定环的长度：相遇点必在环内，继续向前走知道回到这个点即可知环的长度。确定环的入口：设表头到入口为x，入口到快慢指针相遇点为y，相遇点到环的入口为z，环长为L。二者相遇时，快指针走过了2*s=x+y+n*L（快指针在相遇前可能已经在环内饶了若干圈）,慢指针走过了s=x+y，可求得x+y=n*L。由于y+z=L, 故x=(n-1)*L+z。即让一个指针处于相遇点，一个指针处于链表头部，二者同时同速度向前走，当第二个指针走了x步到环的入口时，第一个指针走了(n-1)*L+z步正好也到了环入口
