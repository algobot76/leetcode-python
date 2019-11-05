class TwoSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.count = {}

    def add(self, number):
        """
        Add the number to an internal data structure..
        """
        self.count[number] = self.count.get(number, 0) + 1

    def find(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        """
        for num in self.count:
            if value - num in self.count and (
                    value - num != num or self.count[num] > 1):
                return True
        return False

# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)
