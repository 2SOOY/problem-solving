# 공항
# https://www.acmicpc.net/problem/10775
import sys
sys.setrecursionlimit(10 ** 8)

def find_root(parents, cur):
    if cur != parents[cur]:
        parents[cur] = find_root(parents, parents[cur])
    
    return parents[cur]

def solution(G, planes):
    answer = 0
    parents = [i for i in range(G + 1)] # 다음 추가할 게이트

    for plane in planes:
        root = find_root(parents, plane)
        # 더 이상 추가할 게이트 X
        if root == 0:
            break

        parents[root] = root - 1 # 다음 추가할 게이트 갱신
        answer += 1
        
    return answer

G = int(input())
P = int(input())
planes = [int(input()) for _ in range(P)]

print(solution(G, planes))