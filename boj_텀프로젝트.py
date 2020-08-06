# 텀 프로젝트
# https://www.acmicpc.net/problem/9466
import sys
sys.setrecursionlimit(10 ** 6)

def dfs(students, visited, finished, cur_idx):
    global count
    visited[cur_idx] = True
    next_idx = students[cur_idx] # 인접 노드

    if visited[next_idx] == False:
        dfs(students, visited, finished, next_idx)
    
    else:
        # 다음 정점이 이미 방문 상태(visited)인데, 탐색(finished)이 끝나지 않은 경우
        # cycle 발생
        if finished[next_idx] == False:
            # 사이클을 이루는 노드 개수 세기
            while cur_idx != next_idx:
                count += 1
                next_idx = students[next_idx]
            count += 1 # 자기 자신
    
    finished[cur_idx] = True # 내 정점에 대한 인접 노드 탐색 완료


def solution(number, students):
    global count
    answer = 0
    students = [student - 1 for student in students]
    visited = [False] * len(students) # 정점 방문 여부 배열
    finished = [False] * len(students) # 사이클 생성 여부 파악용 배열 **

    for idx in range(len(students)):
        if visited[idx] == False:
            dfs(students, visited, finished, idx)

    answer = len(students) - count

    return answer


T = int(input())
for _ in range(T):
    count = 0
    num = int(input())
    students = list(map(int, input().split()))

    print(solution(num, students))