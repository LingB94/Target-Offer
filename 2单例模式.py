class singleTon(object):
    instance = {}
    def __new__(cls, *args, **kw):
        if cls not in cls.instance:
            cls.instance[cls] = super(singleTon, cls).__new__(cls)
        return cls.instance[cls]

class testClass(singleTon):
    def __init__(self, n = 1):
        self.coef = n
if __name__ == '__main__':
    a = testClass(1)
    b = testClass(2)
    print(a.coef, b.coef)
    print(type(a), type(b))
    print(a == b)

