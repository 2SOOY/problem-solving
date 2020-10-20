# 로프
# https://www.acmicpc.net/problem/2217

# 풀이 1. 정렬 후, 로프 자체를 이용해 최대 중량 갱신
def solution(N, ropes):
    answer = 0
    ropes.sort(reverse=True) # 질량이 높은 순서대로 정렬 => 들 수 있는 최대값의 질량 구하기 위함

    # 최소 무게 * 현재 로프 개수 => 최대 질량
    for i in range(N):
        temp_weight = ropes[i] * (i + 1)
        answer = max(answer, temp_weight)

    return answer


# 풀이2. 체크 테이블을 이용한 풀이
def solution2(N, ropes):
    answer = 0
    MAX_VAL = max(ropes)
    check = [0] * (MAX_VAL + 1) # 로프 표시를 위한 table

    # 각각의 로프 체크하기
    for rope in ropes:
        check[rope] += 1

    # 최대 중량 구하기 => 뒤에서부터 탐색
    rope_num = 0
    for rope in range(MAX_VAL, 0, -1):
        if check[rope] == 0:
            continue

        rope_num += check[rope] # 현재까지 사용한 로프 개수 추가
        answer = max(answer, rope_num * rope) # 최대 중량 갱신

    return answer

N = int(input())
ropes = [int(input()) for _ in range(N)]
print(solution2(N, ropes))