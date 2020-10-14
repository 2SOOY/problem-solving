# 저울
# https://www.acmicpc.net/problem/2437

def solution(N, sinkers):
    sinkers.sort()
    answer = 0 # 측정 가능한 최소 무게

    # 추를 가지고 1 ~ N까지 만들 수 있고 다음 추가 M 이라면
    # 다음에는 M ~ M + N 까지 만들 수 있다.
    # 1 ~ N, M ~ M + N
    # 즉 M이 N + 1 보다 클 경우 N 과 M 사이에 공백이 생긴다. => 정답
    
    # ex1) 1 ~ 3까지 만들 수 있는 상태, 다음 숫자 4
    # 1, 2, 3, 4, 5, 6, 7 가능
    # ex2) 1 ~ 3까지 만들 수 있는 상태, 다음 숫자 5
    # 1, 2, 3, 5, 6, 7, 8 => 4를 만들 방법이 없음
    for weight in sinkers:
        if weight <= answer + 1:
            answer += weight
        else:
            break

    return answer + 1


N = int(input())
sinkers = list(map(int, input().split()))
print(solution(N, sinkers))