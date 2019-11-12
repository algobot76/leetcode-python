from random import randint


class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = []
        self.positions = {}

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.positions:
            return False

        self.data.append(val)
        self.positions[val] = len(self.data) - 1
        return True

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.positions:
            return False

        idx, last = self.positions[val], self.data[-1]
        self.data[idx], self.positions[last] = last, idx
        self.data.pop()
        del self.positions[val]
        return True

    def getRandom(self):
        """
        Get a random element from the set.
        """
        return self.data[randint(0, len(self.data) - 1)]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
