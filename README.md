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

[24:反转链表](https://github.com/LingB94/Target-Offer/blob/master/24%E5%8F%8D%E8%BD%AC%E9%93%BE%E8%A1%A8.py)
定义三个指针分别指向某点、该点前缀、该点后继

[25:合并两个排序的链表](https://github.com/LingB94/Target-Offer/blob/master/25%E5%90%88%E5%B9%B6%E4%B8%A4%E4%B8%AA%E6%8E%92%E5%BA%8F%E7%9A%84%E9%93%BE%E8%A1%A8.py)
每次比较头结点，将较小的拿出来做新的链表节点，注意处理链表为空的情况

[26:树的子结构](https://github.com/LingB94/Target-Offer/blob/master/26%E6%A0%91%E7%9A%84%E5%AD%90%E7%BB%93%E6%9E%84.py)
找到树中节点值与待比较树根节点相等的点，递归比较其子节点。可以用isclos()函数比较两个浮点数的大小

[27:二叉树的镜像](https://github.com/LingB94/Target-Offer/blob/master/27%E4%BA%8C%E5%8F%89%E6%A0%91%E7%9A%84%E9%95%9C%E5%83%8F.py)
将二叉树根的左右子节点交换，再递归继续完成镜像操作。注意当左右子节点有一个为空的情况时仍然要交换。

[28:对称的二叉树](https://github.com/LingB94/Target-Offer/blob/master/28%E5%AF%B9%E7%A7%B0%E7%9A%84%E4%BA%8C%E5%8F%89%E6%A0%91.py)
类似前序遍历，比较根，比较它的左右子树，注意要将子节电为空的情况考虑进来

[29:顺时针打印矩阵](https://github.com/LingB94/Target-Offer/blob/master/29%E9%A1%BA%E6%97%B6%E9%92%88%E6%89%93%E5%8D%B0%E7%9F%A9%E9%98%B5.py)
打印m*n矩阵的外圈需要四步：打印(0,0)到(0,n-1)；打印(1,n-1)到(m-1,n-1)；打印(m-1,n-2)到(m-1,0)；打印（m-2,0)搭(1,0)。打印的最后一圈可能是一个数字，也可能是一圈，其左上角元素坐标*2均小于矩阵的行数和列数。注意判断打印的四个步骤需要在什么条件下完成

[30:包含min函数的栈](https://github.com/LingB94/Target-Offer/blob/master/30%E5%8C%85%E5%90%ABmin%E5%87%BD%E6%95%B0%E7%9A%84%E6%A0%88.py)
保留两个大小一样的栈，新元素入A栈，如果它比B栈的头顶元素小，则也入B栈，否则，将B栈的头顶元素复制一个再入B栈。

[31:栈的压入、弹出序列](https://github.com/LingB94/Target-Offer/blob/master/31%E6%A0%88%E7%9A%84%E5%8E%8B%E5%85%A5%E5%BC%B9%E5%87%BA%E5%BA%8F%E5%88%97.py)
将压栈序列中的元素逐个入辅助栈，每次入栈时检查其是否是弹出序列的第一个，如果是则从辅助栈中弹出，并将弹出序列中要比较的元素向后移一位。结束后所有元素要么入辅助栈，要么被确定为符合弹出序列的部分，则辅助栈中剩下的元素应和弹出序列中剩下的元素顺序一致。

[32:从上到下打印二叉树](https://github.com/LingB94/Target-Offer/blob/master/32%E4%BB%8E%E4%B8%8A%E5%88%B0%E4%B8%8B%E6%89%93%E5%8D%B0%E4%BA%8C%E5%8F%89%E6%A0%91.py)
问题一：不分行从上到下打印即层序遍历，创建一个队列，每次打印某节点时，将该节点的左右孩子依次入队。问题而：分行从上到下打印，即在层序遍历的基础上增加两个变量toBeprint和nextlevel，toBeprint表示这一层还要打印多少个，nextlevel表示下一层要打印多少个。当toBeprint为0时打印换行符，并将nextlevel的值赋给它即可。问题三：之字形打印二叉树，用两个辅助栈分别处理奇数层和偶数层（本题中层数从0开始算起）。打印奇数层元素时，将该元素的孩子先左后右存入偶数层栈，打印偶数层元素时，将该元素的孩子先右后左存入奇数层栈。

[33:二叉搜索树的后序遍历](https://github.com/LingB94/Target-Offer/blob/master/33%E4%BA%8C%E5%8F%89%E6%90%9C%E7%B4%A2%E6%A0%91%E7%9A%84%E5%90%8E%E5%BA%8F%E9%81%8D%E5%8E%86%E5%BA%8F%E5%88%97.py)
递归完成，序列的最后一个元素为根节点，从头开始遍历完所有比它小的连续元素，这是它的左子树，其后的元素为它的右子树。递归判断左右子树是否符合二叉搜索树的条件，即左子树全都小于根，右子树全都大于根。

[34:二叉树中和为某值的路径](https://github.com/LingB94/Target-Offer/blob/master/34%E4%BA%8C%E5%8F%89%E6%A0%91%E4%B8%AD%E5%92%8C%E4%B8%BA%E6%9F%90%E5%80%BC%E7%9A%84%E8%B7%AF%E5%BE%84.py)
深度优先遍历的同时记录访问到的节点和节点值之和。用一个栈保存访问到某个节点时的路径和，一个栈保存当前经过的路径。递归地访问某个节点和它的子节点，到叶节点时如果路径和等于某值，则将该路径记录到result，否则从两个栈中弹出栈顶元素。

[35:复杂链表的赋值](https://github.com/LingB94/Target-Offer/blob/master/35%E5%A4%8D%E6%9D%82%E9%93%BE%E8%A1%A8%E7%9A%84%E5%A4%8D%E5%88%B6.py)
分三步完成：将各点的复制点放在原点的后面并串成一个链表；各复制点的sibling指向的点即原点的sibling的下一个点；将链表拆成原点链表和复制链表

[36:二叉搜索树与双向链表](https://github.com/LingB94/Target-Offer/blob/master/36%E4%BA%8C%E5%8F%89%E6%90%9C%E7%B4%A2%E6%A0%91%E4%B8%8E%E5%8F%8C%E5%90%91%E9%93%BE%E8%A1%A8.py)
中序遍历递归地将树的左指针指向比它小的数中最大的那个，将树的右指针指向比它大的数中最小的那个，设定plast指向已经排好序的链表中最大的节点，对访问到的节点处理为：plast的右指针（如果存在）指向访问节点，访问节点的左指针指向plast，plast指向T

[37:序列化二叉树](https://github.com/LingB94/Target-Offer/blob/master/37%E5%BA%8F%E5%88%97%E5%8C%96%E4%BA%8C%E5%8F%89%E6%A0%91.py)
序列化即前序遍历整个树，将访问到的节点存入result，如果节点为空则存入一个非数字的符号。反序列化用一个全局变量step记录当前访问到列表中的第几个元素，用isdigit()判断元素是否为非数字符号，如果是则返回None，不是则利用step构造其左右子树

[38:字符串的排列](https://github.com/LingB94/Target-Offer/blob/master/38%E5%AD%97%E7%AC%A6%E4%B8%B2%E7%9A%84%E6%8E%92%E5%88%97.py)
第一种方法，递归地确定第一个位置的字符和后续字符串的排列；第二种方法，利用itertools.permutations的内置函数。第一种方法要将字符串先列表化再排序，这样才能处理字符串中存在重复字符的情况。

[39:数组中出现次数超过一半的数字](https://github.com/LingB94/Target-Offer/blob/master/39%E6%95%B0%E7%BB%84%E4%B8%AD%E5%87%BA%E7%8E%B0%E6%AC%A1%E6%95%B0%E8%B6%85%E8%BF%87%E4%B8%80%E5%8D%8A%E7%9A%84%E6%95%B0%E5%AD%97.py)
第一种方法，类似快速排序中将比pivot小的数都放到它前面，比它大的都放到它后面，出现次数超过一半的数字必然位于中位数上。快速排序中每次排序后都返回pivot在排序后所应当在的位置，可以判断其是否在中间位。第二种方法，设两个变量，result初始值为列表中的第一个元素，cnt初始值为1，记录result的出现次数比其他的相对多寡。遍历列表时，碰到不同于result的数，则cnt减1，当cnt减为0时，表明其他数的出现次数多于result，此时将result设为最新的数，cnt计1,最后的result必为出现次数最多的那个。注意两种方法都要最后检查result是不是出现次数多于一半。

[40:最小的k个数](https://github.com/LingB94/Target-Offer/blob/master/40%E6%9C%80%E5%B0%8F%E7%9A%84k%E4%B8%AA%E6%95%B0.py)
第一种方法，基于快速排序的partition函数，不断计算pivot的最终位置直至其位于第k位。第二种方法，建立一个大小为k的最大堆，python中的heapq只实现了最小堆，可以将数字的相反数存入最小堆来实现最大堆。每读入一个新元素，将其与堆中最大元素比较看是否要替换到堆里。这种方法可以解决大规模数据的情况

[41:数据流中的中位数](https://github.com/LingB94/Target-Offer/blob/master/41%E6%95%B0%E6%8D%AE%E6%B5%81%E4%B8%AD%E7%9A%84%E4%B8%AD%E4%BD%8D%E6%95%B0.py)
将所有数据平分为两部分，小的部分用最大堆，大的用最小堆。当容器中的数有偶数个时，新元素插入最小堆，否则插入最大堆。插入最小堆时要保证最小堆中的元素都比最大堆中的元素大，可以先检查最大堆中的元素与新元素的大小，如果新元素比最大堆中的最大元素小，则用新元素替换最大堆中的最大元素，并将该最大元素存入最小堆；否则正常插入最小堆。注意heapq只支持最小堆，因此存入最大堆或取出最大堆的元素要乘以-1，在本题中有两个地方没改（懒...）

[42:连续子数组的最大和](https://github.com/LingB94/Target-Offer/blob/master/42%E8%BF%9E%E7%BB%AD%E5%AD%90%E6%95%B0%E7%BB%84%E7%9A%84%E6%9C%80%E5%A4%A7%E5%92%8C.py)
设置tmpSum初始值为0，记录当前某序列的和，maxSum初始值为l[0]，已经找到的最大和，maxSum设为l[0]可以解决序列中全部为负数的情况。顺序遍历整个数组并累加各元素，当tmpSum<=0时，表明后面的数与现在的序列和相加不会变的更大，此时将tmpSum设为0继续遍历和累加

[43:1~n中1出现的次数](https://github.com/LingB94/Target-Offer/blob/master/43%E8%AE%A1%E7%AE%971%E5%88%B0n%E4%B8%AD1%E5%87%BA%E7%8E%B0%E7%9A%84%E6%AC%A1%E6%95%B0.py)
分两种情况，最高位为1和最高位不为1。以5位数为例，对12345，现计算1到9999有多少个1，再计算10000到12345中的1次数。1到9的1个数为1,1到99的1个数为19=10+9*1,1到999的1个数为271=100+9*19，以此规律可以计算1到99...9之间1的个数。10000到12345之间最高位的1出现次数即12345-10000+1。再加上递归计算的2345的1次数即可。若高位不为1，例如32345，则先计算1到9999，再计算10000到19999,20000到29999中1的个数，再递归计算30000到32345，即1-2345中1的个数即可。

[44:数字序列中某一位的数字](https://github.com/LingB94/Target-Offer/blob/master/44%E6%95%B0%E5%AD%97%E5%BA%8F%E5%88%97%E4%B8%AD%E6%9F%90%E4%B8%80%E4%BD%8D%E7%9A%84%E6%95%B0%E5%AD%97.py)
0到9共10个，10到99共90个，100到999共900个，以此可以计算出第n个数位于哪个区间（几位数）。计算出第n个数是哪一个数中的某一位即可

[45:把数组排成最小的数](https://github.com/LingB94/Target-Offer/blob/master/45%E6%8A%8A%E6%95%B0%E7%BB%84%E6%8E%92%E6%88%90%E6%9C%80%E5%B0%8F%E7%9A%84%E6%95%B0.py)
新定义一种排序规则，如果a拼b比b拼a小，则a在排序中位于b前，将数组从小到大排序之后拼接在一起即最小的数

[46:把数字翻译成字符串](https://github.com/LingB94/Target-Offer/blob/master/46%E6%8A%8A%E6%95%B0%E5%AD%97%E7%BF%BB%E8%AF%91%E6%88%90%E5%AD%97%E7%AC%A6%E4%B8%B2.py)
从上到下递归如果存在重复，可以考虑从下往上递归。在本题中即从右往左查看。

[47:礼物的最大价值](https://github.com/LingB94/Target-Offer/blob/master/47%E7%A4%BC%E7%89%A9%E7%9A%84%E6%9C%80%E5%A4%A7%E4%BB%B7%E5%80%BC.py)
(i,j)为终点的礼物价值仅依赖于(i-1,j)和(i,j-1)处的最大礼物价值。设矩阵的行、列数为m,n。设(i,j)处礼物最大价值为f(i,j)，定义一个长度为n的列表l，访问到(i,j)时，l[0]到l[j-1]存放f(i,0)到f(i,j-1)，l[j]到l[n-1]存放f(i-1,j)到f(i-1,n-1)

[48:最常不含重复字符的子字符串](https://github.com/LingB94/Target-Offer/blob/master/48%E6%9C%80%E5%B8%B8%E4%B8%8D%E5%90%AB%E9%87%8D%E5%A4%8D%E5%AD%97%E7%AC%A6%E7%9A%84%E5%AD%90%E5%AD%97%E7%AC%A6%E4%B8%B2.py)
定义一个长度为26的列表记录每个字母上次出现的位置，初始值为-1。定义curLength, maxLength分别记录当前子字符串的长度，已找到的最大子字符串长度。遍历到某个字符时，如果它上次出现的位置不在当前子字符串内，则当前子字符串可继续增加，否则将当前子字符串换为上一个重复字符到当前位置的子字符串

[49:丑数](https://github.com/LingB94/Target-Offer/blob/master/49%E4%B8%91%E6%95%B0.py)
创建一个从小到大仅存放丑数的列表，第一个值为1，对于列表中的每个丑数，分别乘以2、3、5，直到找到第一个比已有丑数大的新丑数。

[50:第一个只出现一次的字符](https://github.com/LingB94/Target-Offer/blob/master/50%E7%AC%AC%E4%B8%80%E4%B8%AA%E5%8F%AA%E5%87%BA%E7%8E%B0%E4%B8%80%E6%AC%A1%E7%9A%84%E5%AD%97%E7%AC%A6.py)
创建一个字典，key为遍历到的字符，值为它出现的次数。创建完字典后再次遍历字符串，直至找到第一个值为1的字符

[51:数组中的逆序对](https://github.com/LingB94/Target-Offer/blob/master/51%E6%95%B0%E7%BB%84%E4%B8%AD%E7%9A%84%E9%80%86%E5%BA%8F%E5%AF%B9.py)
类似归并排序，将数组分为左右两半，分别计算其中的逆序数并排序，再计算跨数组之间的逆序数并将其合并为新的排序数组

[52:两个链表中的第一个公共节点](https://github.com/LingB94/Target-Offer/blob/master/52%E4%B8%A4%E4%B8%AA%E9%93%BE%E8%A1%A8%E7%9A%84%E7%AC%AC%E4%B8%80%E4%B8%AA%E5%85%AC%E5%85%B1%E8%8A%82%E7%82%B9.py)
遍历两个链表得到其长度，较长的那个先走若干步让剩下的节点数与另一个链表一样，然后二者一起遍历直至找到公共节点

[53:在排序数组中查找数字](https://github.com/LingB94/Target-Offer/blob/master/53%E5%9C%A8%E6%8E%92%E5%BA%8F%E6%95%B0%E7%BB%84%E4%B8%AD%E6%9F%A5%E6%89%BE%E6%95%B0%E5%AD%97.py)
用二分查找找到第一个k和最后一个k

[54:二叉搜索树的第k大节点](https://github.com/LingB94/Target-Offer/blob/master/54%E4%BA%8C%E5%8F%89%E6%90%9C%E7%B4%A2%E6%A0%91%E7%9A%84%E7%AC%ACk%E4%B8%AA%E8%8A%82%E7%82%B9.py)
中序遍历后返回第k个节点

[55:二叉树的深度](https://github.com/LingB94/Target-Offer/blob/master/55%E4%BA%8C%E5%8F%89%E6%A0%91%E7%9A%84%E6%B7%B1%E5%BA%A6.py)
后序遍历，算出左右子树的深度，较大者加1

[56:数组中数字出现的次数](https://github.com/LingB94/Target-Offer/blob/master/56%E6%95%B0%E7%BB%84%E4%B8%AD%E6%95%B0%E5%AD%97%E5%87%BA%E7%8E%B0%E7%9A%84%E6%AC%A1%E6%95%B0.py)
题目一：数组中只出现一次的两个数字。因为一个数异或它本身为零，故所有数异或的结果为两个仅出现一次数的异或结果，这两个数不相等故异或结果至少有一位为1，根据该位是否为1将数组分为两个，分别在两个数组内异或。
题目二：数组中唯一只出现一次的数字。创建一个长度为32的列表记录所有数字的二进制表示中各位上的1出现的次数，最后每一位上的数字对3取与即得到只出现一次的数字的二进制表示

[57:和为s的数字](https://github.com/LingB94/Target-Offer/blob/master/57%E5%92%8C%E4%B8%BAs%E7%9A%84%E6%95%B0%E5%AD%97.py)
题目一：和为s的两个数字。设两个指针分别指向数组的第一个和最后一个，如果相加小于s，则第一个指针向后移；相加大于s，则第二个指针向前移。
题目二：和为s的连续正数序列。设两个指针分别指向数组的第一个和第二个（start,end）。start最多到s//2，若start到end之间和小于s，则end向后移；若大于s，则start向后移。

[58:翻转字符串](https://github.com/LingB94/Target-Offer/blob/master/58%E7%BF%BB%E8%BD%AC%E5%AD%97%E7%AC%A6%E4%B8%B2.py)
题目一：翻转字符串。将字符串按空格分开，逆序存入一个列表，注意存的时候加入空格。
题目二：左旋转字符串。书上的方法：翻转前k个，翻转后n-k个，翻转整个字符串。python中用切片即可

[60:n个骰子的点数](https://github.com/LingB94/Target-Offer/blob/master/60n%E4%B8%AA%E9%AA%B0%E5%AD%90%E7%9A%84%E7%82%B9%E6%95%B0.py)
设置两个数组，一个的第n位表示当前和为n的次数，另一个表示再投一个骰子后可能的点数和出现的次数，比如下标为n时它的值等于第一个数组中下标为n-1,n-2,...,n-6的次数之和。

[61:扑克牌中的顺子](https://github.com/LingB94/Target-Offer/blob/master/61%E6%89%91%E5%85%8B%E7%89%8C%E4%B8%AD%E7%9A%84%E9%A1%BA%E5%AD%90.py)
将字符串转化为数字后排序，计算其中0出现的次数和数字之间的空档，相等则构成顺子

[62:圆圈中剩下的数字](https://github.com/LingB94/Target-Offer/blob/master/62%E5%9C%86%E5%9C%88%E4%B8%AD%E5%89%A9%E4%B8%8B%E7%9A%84%E6%95%B0%E5%AD%97.py)
f(n,m)表示n个数删去第m个后剩下数的编号，f(n,m) = (f(n-1,m)+m)%n, f(0,m)=0

[63:股票的最大利润](https://github.com/LingB94/Target-Offer/blob/master/63%E8%82%A1%E7%A5%A8%E7%9A%84%E6%9C%80%E5%A4%A7%E5%88%A9%E6%B6%A6.py)
找到数组中最小和最大的数且最小的要位于最大的前面。

[64:求1+2+。。。+n](https://github.com/LingB94/Target-Offer/blob/master/64%E6%B1%821%2B2%2B...%2Bn.py)
非零数两次取反为True,零两次取反为False。设置一个存放函数的字典，key为True时递归加法，key为False时返回0

[65:不用加减乘除做加法](https://github.com/LingB94/Target-Offer/blob/master/65%E4%B8%8D%E7%94%A8%E5%8A%A0%E5%87%8F%E4%B9%98%E9%99%A4%E5%81%9A%E5%8A%A0%E6%B3%95.py)
为处理负数加的情况，需要模拟溢出。设置最大值为2**32，大于这个数的操作会使用这个数的相反数。不考虑进位，二进制数各位相加的结果等于各位异或；进位相当于各位进行与操作，循环将这两步算出的结果相加

[66:构建乘积数组](https://github.com/LingB94/Target-Offer/blob/master/66%E6%9E%84%E5%BB%BA%E4%B9%98%E7%A7%AF%E6%95%B0%E7%BB%84.py)
B[i]=(A[0]*A[1]*...*A[i-1])*(A[i+1]*...*A[n-1) = C[i]*D[i], C[i] = C[i-1]*A[i-1], D[i]=D[i+1]*A[i+1], C[0]=1,D[n-1]=A[n-1]，这道题对C[i]的计算写错了，应该是result[i] = result[i-1]*l[i-1]
