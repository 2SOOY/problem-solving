# 77. Combinations
# https://leetcode.com/problems/combinations/


def combine(n, k):
    checked = [False] * n
    result = []

    def dfs(start, path):
        if len(path) == k:
            result.append(path[:])
            return
        
        for idx in range(start, n):
            if checked[idx]:
                continue

            checked[idx] = True
            path.append(idx + 1)
            dfs(idx + 1, path)
            path.pop()
            checked[idx] = False

    dfs(0, [])
    return result

n, k = 5, 3
print(combine(n, k))
        