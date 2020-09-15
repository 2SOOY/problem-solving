# 39. Combination Sum
# https://leetcode.com/problems/combination-sum/

def combinationSum(candidates, target):
    result = []

    def dfs(start, path):
        if sum(path) > target:
            return

        if sum(path) == target:
            result.append(path[:])
            return
        
        for idx in range(start, len(candidates)):
            path.append(candidates[idx])
            dfs(idx, path)
            path.pop()

    dfs(0, [])
    return result

candidates = [2,3,5]
target = 8
print(combinationSum(candidates, target))    