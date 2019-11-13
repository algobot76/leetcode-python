import collections


class MovingAverage:

    def __init__(self, size):
        """
        Initialize your data structure here.
        """
        self.q = collections.deque()
        self.sum_ = 0
        self.size = size

    def next(self, val):
        self.q.append(val)
        self.sum_ += val
        if len(self.q) > self.size:
            self.sum_ -= self.q.popleft()
        return self.sum_ / len(self.q)

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
