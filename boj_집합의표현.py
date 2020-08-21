# 집합의 표현
# https://www.acmicpc.net/problem/1717

UNION, IS_SAME = 0, 1

def find_parent(parents, num):
    if parents[num] != num:
        parents[num] = find_parent(parents, parents[num])
    
    return parents[num]

def union_sets(parents, a, b):
    root_a = find_parent(parents, a)
    root_b = find_parent(parents, b)

    if root_a == root_b:
        return
    
    # 큰 수가 부모가 되도록 합치기
    if root_a < root_b:
        parents[root_a] = root_b
    else:
        parents[root_b] = root_a

def is_same_set(parents, a, b):
    root_a = find_parent(parents, a)
    root_b = find_parent(parents, b)

    if root_a == root_b:
        print('YES')
    else:
        print('NO')


def solution(parents, flag, a, b):
    if flag == UNION:
        union_sets(parents, a, b)
        print(parents)
    else:
        is_same_set(parents, a, b)


N, M = map(int, input().split())
parents = [num for num in range(N + 1)]

for _ in range(M):
    flag, a, b = map(int, input().split())
    solution(parents, flag, a, b)