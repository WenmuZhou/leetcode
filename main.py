class MyStack:

    def __init__(self):
        self.queueA = []
        self.queueB = []

    def push(self, node):
        self.queueA.insert(0, node)

    def pop(self):
        if self.empty():
            return None
        while len(self.queueA) != 0:
            self.queueB.append(self.queueA.pop())
        return self.queueB.pop()

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        if self.empty():
            return None
        while len(self.queueA) != 0:
            self.queueB.append(self.queueA.pop())
        return self.queueB[-1]

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return len(self.queueA) == 0 and len(self.queueB) == 0

if __name__ == '__main__':
    obj = MyStack()
    print(obj.push(1))
    print(obj.push(2))
    print(obj.top())
    print(obj.pop())
    print(obj.empty())