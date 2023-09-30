class Solution:
    def countOrders(self, n):
        if n == 1:
            return 1

        ans = self.countOrders(n - 1)

        mod = (10 ** 9) + 7

        cal = (n * (2 * n - 1))

        return cal * ans % mod





