# Target-Offer
剑指offer第二版-python3实现

[2:单例模式singleton](https://github.com/LingB94/Target-Offer/blob/master/2%E5%8D%95%E4%BE%8B%E6%A8%A1%E5%BC%8F.py)
单例模式即使某个类只能访问一个唯一的对象（例如一个班只能有一个班主任）。python中的构造方法分为创建对象和初始化对象两步，前者使用__new__，后者使用__init__。new方法必须有一个参数clf表示要实例化的类（如班主任），同时要返回一个对象。在singleton类中定义一个用于存放类名的set，如果创建对象时这个set中没有“班主任”类，则正常创建，否则返回“班主任”。这样在使用班主任类创建两个变量时，因为new在init之前执行，这两个变量只能指向同一个对象。

[另一种解决方法](https://github.com/LingB94/Target-Offer/blob/master/2(1)%E5%8D%95%E4%BE%8B%E6%A8%A1%E5%BC%8F.py)
利用装饰器。装饰器是返回值为函数的函数，将它放在类定义的前面，我们就会在使用某个类（班主任）时自动将该类作为装饰器的输入参数。可以在装饰器函数内部定义一个用于存放类名的set，让装饰器返回的函数仅返回在set中“班主任”类。两种单例模式的方法都用到了python中的set，set即集合，其中不允许重复。

[4:二维数组中的查找](https://github.com/LingB94/Target-Offer/blob/master/4%E4%BA%8C%E7%BB%B4%E6%95%B0%E7%BB%84%E4%B8%AD%E7%9A%84%E6%9F%A5%E6%89%BE.py)
矩阵从上到下递增，从左到右递增。从矩阵的左下角开始找起。左下角的元素必然比它所在列的所有元素都大，比它所在行的所有元素都小。如果左下角的元素比目标元素大，则排除最后一行，如果比目标元素小，则排除第一列。
