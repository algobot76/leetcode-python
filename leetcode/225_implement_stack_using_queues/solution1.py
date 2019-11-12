from collections import deque


class MyQueue:
    def __init__(self):
        self.data = deque()

    def push(self, x):
        self.data.append(x)

    def pop(self):
        return self.data.popleft()

    def peak(self):
        return self.data[0]

    def empty(self):
        return len(self.data) == 0

    def size(self):
        return len(self.data)


class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q = MyQueue()

    def push(self, x):
        """
        Push element x onto stack.
        """
        self.q.push(x)
        for _ in range(self.q.size() - 1):
            self.q.push(self.q.pop())

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.q.pop()

    def top(self):
        """
        Get the top element.
        """
        return self.q.peak()

    def empty(self):
        """
        Returns whether the stack is empty.
        """
        return self.q.empty()

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
