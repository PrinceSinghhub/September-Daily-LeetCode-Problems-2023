class Solution:
    def countBits(self, n: int) -> List[int]:
        # another Approch
        # f = [0] * (num + 1)
        # for i in range(1, num + 1):
        #     f[i] = f[i >> 1] + (i & 1)
        # return f

        ans = [0] * (n + 1)

        for i in range(1, n + 1):
            ans[i] = ans[i // 2] + i % 2

        return ans


