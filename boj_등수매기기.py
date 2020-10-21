# 등수 매기기
# https://www.acmicpc.net/problem/2012

def solution(N, grades):
    answer = 0

    grades.sort()
    for grade in range(1, N + 1):
        answer += abs(grade - grades[grade - 1])

    return answer

N = int(input())
grades = [int(input()) for _ in range(N)]
print(solution(N, grades))
