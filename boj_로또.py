# 로또
# https://www.acmicpc.net/problem/6603
import sys
sys.setrecursionlimit(10 ** 8)

SIX = 6

def solution(k, numbers):
    check = [False] * k

    def dfs(level, start, result):
        if level == SIX:
            result = map(str, result)
            print(' '.join(result))
            return
        
        for i in range(start, k):
            if check[i]:
                continue

            check[i] = True
            dfs(level + 1, i + 1, result + [numbers[i]])
            check[i] = False

    dfs(0, 0, [])
    return

while True:
    inputs = list(map(int, input().split()))
    if len(inputs) == 1:
        break

    k, numbers = inputs[0], inputs[1:]
    solution(k, numbers)
    print()