def Fib_rec(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return Fib_rec(n-1) + Fib_rec(n-2)

def Fib_iter(n):
    a, b = 0, 1
    i = 0
    while(i < n):
        a, b = b, a+b
        i+=1
    return a

def Fib_generator(n):
    i, a, b = 0, 0, 1
    while(i < n):
        a, b = b, a+b
        yield a
        i+=1

if __name__ == '__main__':
    print(Fib_rec(5))
    print(Fib_iter(5))
    print(Fib_generator(5))
    g = Fib_generator(5)
    print(next(g))
    print(next(g))
    print(next(g))
    print(next(g))
    print(next(g))
    print(next(g))

