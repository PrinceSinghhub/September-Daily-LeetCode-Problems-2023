class Solution:
    def sortArrayByParity(self, nums):

        even = []
        old = []

        for i in nums:
            if i % 2 == 0:
                even.append(i)
            else:
                old.append(i)

        even.extend(old)
        return even