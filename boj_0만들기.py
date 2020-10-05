# 0 만들기
# https://www.acmicpc.net/problem/7490

def calculate(expression):
    expression = expression.replace(' ', '')
    return eval(expression)

def solution(n):
    seq = list(range(1, n + 1))
    candidates = []

    # 연산자 조합 구하기
    def dfs(level, path):
        if level == n - 1:
            candidates.append(path[:])
            return
        
        dfs(level + 1, path + [' '])
        dfs(level + 1, path + ['+'])
        dfs(level + 1, path + ['-'])

    dfs(0, []) # N - 1개의 연산자 조합 구하기

    # 계산
    for candidate in candidates:
        path = str(seq[0])
        for i in range(len(candidate)):
            path += candidate[i] + str(seq[i + 1])

        if calculate(path) == 0:
            print(path)

    return

# MAIN
T = int(input())
for i in range(T):
    n = int(input())
    solution(n)
    print()
