# 캠핑
# https://www.acmicpc.net/problem/4796

def print_answer(idx, answer):
    print('Case {0}: {1}'.format(idx, answer))
    return

def solution(L, P, V):
    answer = 0
    # 1. V // P * L 만큼 카운트 가능
    answer = (V // P) * L
    
    # 2. V % P 를 기준으로 L과 비교하여 나머지 일자 계산
    temp = V % P
    if temp > L:
        answer += L
    else:
        answer += temp

    return answer

index = 0
while True:
    L, P, V = map(int, input().split())
    if L == 0 and P == 0 and V == 0:
        break
    
    index += 1
    answer = solution(L, P, V)
    print_answer(index, answer)