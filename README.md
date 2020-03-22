# Target-Offer
剑指offer第二版-python3实现

[2:单例模式singleton](https://github.com/LingB94/Target-Offer/blob/master/2%E5%8D%95%E4%BE%8B%E6%A8%A1%E5%BC%8F.py)
单例模式即使某个类只能访问一个唯一的对象（例如一个班只能有一个班主任）。python中的构造方法分为创建对象和初始化对象两步，前者使用__new__，后者使用__init__。new方法必须有一个参数clf表示要实例化的类（如班主任），同时要返回一个对象。在singleton类中定义一个用于存放类名的set，如果创建对象时这个set中没有“班主任”类，则正常创建，否则返回“班主任”。这样在使用班主任类创建两个变量时，因为new在init之前执行，这两个变量只能指向同一个对象。
