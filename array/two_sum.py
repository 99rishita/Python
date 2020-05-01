class Solution:
    def twoSum(self, nums, target):
        sum = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                sum = nums[i] + nums[j]
                if target == sum:
                    return (i, j)
        