# 블랙잭
# https://www.acmicpc.net/problem/2798

def solution(N, M, cards):
    check = [False] * N
    answer = 0 

    # 1. 3개를 선택하는 조합 구하기
    def dfs(count, start, value):
        nonlocal answer
        # 합이 M을 넘지 않은 카드 3장 
        if value > M:
            return

        # 2. 최대한 M에 근접한 값
        if count == 3:
            if M - value < M - answer:
                answer = value
            return

        # 조합 logic
        for i in range(start, N):
            if check[i]:
                continue

            check[i] = True
            dfs(count + 1, i + 1, value + cards[i])
            check[i] = False

    dfs(0, 0, 0)
    return answer

N, M = map(int, input().split())
cards = list(map(int, input().split()))

print(solution(N, M, cards))
