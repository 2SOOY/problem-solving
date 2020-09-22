# 1. Two Sum
# https://leetcode.com/problems/two-sum/

# 방법1 - O(N^2)
def twoSum1(nums, target):
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]   


# 방법2 - O(N)
# a + b = c == a = c - b
def twoSum2(nums, target):
    num_info = {}

    for idx, num in enumerate(nums):
        new_target = target - num

        if new_target in num_info:
            return [num_info[new_target], idx]

        num_info[num] = idx 


nums = [2, 7, 11, 15]
target = 9
print(twoSum1(nums, target))
print(twoSum2(nums, target))