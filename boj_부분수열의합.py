# 부분 수열의 합
# https://www.acmicpc.net/problem/1182

def solution(N, numbers, target):
    answer = 0

    def dfs(count, result):
        nonlocal answer

        if count == N:
            # 공집합 제외 조건 만족 확인 
            if result and sum(result) == target:
                answer += 1
            return

        dfs(count + 1, result + [numbers[count]]) # 숫자 선택 
        dfs(count + 1, result) # 숫자 선택 X
    
    dfs(0, [])

    return answer

N, target = map(int, input().split())
numbers = list(map(int, input().split()))
print(solution(N, numbers, target))