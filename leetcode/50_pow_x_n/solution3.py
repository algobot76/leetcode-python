class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1 / x
            n = -n
        return self.pow_(x, n)

    def pow_(self, x: float, n: int) -> float:
        if n == 0:
            return 1

        half = self.pow_(x, n // 2)
        if n % 2 == 0:
            return half * half
        else:
            return half * half * x
