class Solution:


    def findAllCombinations(self,nums,tar,ans,ds):

        if tar < 0:
            return
        if tar == 0:
            ans.append(ds[:])

        for i in range(len(nums)):

            ds.append(nums[i])
            self.findAllCombinations(nums, tar - nums[i],ans,ds)
            ds.pop()

    # recursion Approch
    def RecuersioncombinationSum4(self, nums,target):

        if target < 0:
            return 0
        if target == 0:
            return 1

        count = 0
        for i in range(len(nums)):
            count += self.RecuersioncombinationSum4(nums, target - nums[i])

        # check all combination
        ans = []
        self.findAllCombinations(nums, target, ans, [])
        print(ans)

        return count

    # memoization Approch
    def MemoizationcombinationSum4(self, nums, target, dp):

        if target < 0:
            return 0
        if target == 0:
            return 1

        if dp[target] != -1:
            return dp[target]

        count = 0
        for i in range(len(nums)):
            count += self.combinationSum4(nums, target - nums[i])

        dp[target] = count
        return dp[target]

    # DP Approch

    def DPcombinationSum4(self, nums, target):

        dp = [0] * (target + 1)

        dp[0] = 1

        # travese from target 1 to target
        for i in range(1, target + 1):

            # traverse on nums
            for j in range(len(nums)):

                if (i - nums[j]) >= 0:
                    dp[i] += dp[i - nums[j]]

        print(dp)
        return dp[target]

    def combinationSum4(self, nums: List[int], target: int) -> int:

        return self.RecuersioncombinationSum4(nums, target)

