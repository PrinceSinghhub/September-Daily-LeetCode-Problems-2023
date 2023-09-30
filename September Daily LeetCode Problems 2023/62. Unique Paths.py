class Solution:
    def uniquePaths(self, row, coll):

        dp = [-1] * coll

        for i in range(row):
            dummy = [-1] * coll
            for j in range(coll):

                if i == 0 and j == 0:
                    dummy[j] = 1
                    continue

                up = 0
                left = 0

                if i > 0:
                    up = dp[j]

                if j > 0:
                    left = dummy[j - 1]

                dummy[j] = up + left

            dp = dummy
        print(dp)
        return dp[coll - 1]
