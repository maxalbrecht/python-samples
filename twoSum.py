"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution
"""
def twoSum(nums, target):
    currentIndex = 0
    while currentIndex < len(nums):
        if (target - nums[currentIndex]) in nums:
            return([currentIndex, nums.index(target - nums[currentIndex])])
        currentIndex += 1

print(twoSum([2,7,11,15], 18))