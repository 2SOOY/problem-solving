# 17. Letter Combinations of a Phone Number
# https://leetcode.com/problems/letter-combinations-of-a-phone-number/

phone_info = {'2': 'abc', '3': 'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}

def letterCombinations(digits):
    result = []
    
    if len(digits) == 0:
        return result

    def dfs1(level, path):
        if level == len(digits):
            result.append(''.join(path))
            return

        for char in phone_info[digits[level]]:
            path.append(char)
            dfs1(level + 1, path)
            path.pop()

    def dfs2(idx, path):
        if len(path) == len(digits):
            result.append(path)
            return
        
        for i in range(idx, len(digits)):
            for char in phone_info[digits[i]]:
                dfs2(i + 1, path + char)

    dfs1(0, [])
    # dfs2(0, '')

    return result

digits = '23'
print(letterCombinations(digits))