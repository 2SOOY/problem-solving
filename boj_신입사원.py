# 신입 사원
# https://www.acmicpc.net/problem/1946
import sys
input = sys.stdin.readline

GRADE, INTERVIEW = 0, 1

def solution(N, people):
    answer = 0
    people.sort()

    score = people[0][INTERVIEW]
    answer += 1

    for cur in range(1, N):
        cur_score = people[cur][INTERVIEW]

        if score > cur_score:
            score = cur_score
            answer += 1

    return answer

T = int(input())
for _ in range(T):
    N = int(input())
    people = [list(map(int, input().split())) for _ in range(N)]

    print(solution(N, people))