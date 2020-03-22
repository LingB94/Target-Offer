import functools

def singleTon1(cls):
    instance = {}
    @functools.wraps(cls)
    def getinstance(*args, **kw):
        if cls not in instance:
            instance[cls] = cls(*args, **kw)
        return instance[cls]
    return getinstance

@singleTon1
class testClass1(object):
    def __init__(self, n = 1):
        self.coef = n

if __name__ == "__main__":
    a = testClass1(1)
    b = testClass1(2)
    print(a.coef, b.coef)
    print(type(a), type(b))
    print(a == b)

