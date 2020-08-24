# TLE
import collections


class FirstUnique:

    def __init__(self, nums):
        self.nums = nums
        self.counts = collections.defaultdict(int)
        for num in self.nums:
            self.counts[num] += 1

    def showFirstUnique(self):
        for num in self.nums:
            if self.counts[num] == 1:
                return num
        return -1

    def add(self, value):
        self.nums.append(value)
        self.counts[value] += 1

# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)
