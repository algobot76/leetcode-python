class Solution:
    def superPow(self, a, b):
        if a == 0:
            return 0
        ans = 1

        def mod(x):
            return x % 1337

        for n in b:
            ans = mod(mod(ans ** 10) * mod(a ** n))

        return ans
