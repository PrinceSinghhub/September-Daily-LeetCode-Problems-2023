class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        check = nums.copy()

        check.sort()

        if nums == check or nums == check[::-1]:
            return True
        return False

#         Max = max(nums)

#         if nums.index(Max) == 0 or nums.index(Max) == len(nums)-1:
#             return True

#         return False
