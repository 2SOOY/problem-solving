# 46. Permutations
# https://leetcode.com/problems/permutations/
from copy import deepcopy

def permute(nums):
    result = []
    checked = [False] * len(nums)
    
    if len(nums) == 0:
        return result
    
    def dfs(idx, path):
        if len(path) == len(nums):
            temp = deepcopy(path)
            result.append(temp)
            return
        
        for i in range(len(nums)):
            if checked[i]:
                continue

            checked[i] = True
            path.append(nums[i])
            dfs(i + 1, path)
            path.pop()
            checked[i] = False
    
    dfs(0, [])
    return result

nums = [1, 2, 3]
print(permute(nums))