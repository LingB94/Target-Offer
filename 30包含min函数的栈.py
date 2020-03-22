class minStack(object):
    def __init__(self):
        self.__stack = []
        self.__min = []

    def push(self, n):
        self.__stack.append(n)
        if(len(self.__min) == 0 or n < self.__min[-1]):
            self.__min.append(n)
        else:
            self.__min.append(self.__min[-1])

    def pop(self):
        if(len(self.__stack) > 0):
            self.__min.pop()
            return self.__stack.pop()
        return False

    def min(self):
        if(len(self.__stack) > 0):
            return self.__min[-1]
        return False

    def printIn(self):
        if(len(self.__stack) > 0):
            print(self.__stack)
            print(self.__min)

if __name__ == '__main__':
    s = minStack()
    s.push(3)
    s.printIn()
    s.push(4)
    s.printIn()
    s.push(2)
    s.printIn()
    s.push(1)
    s.printIn()
    s.pop()
    s.printIn()
    s.pop()
    s.printIn()
    s.push(0)
    s.printIn()