# 여행 가자
# https://www.acmicpc.net/problem/1976

def find_parent(parents, city):
    if city != parents[city]:
        parents[city] = find_parent(parents, parents[city])

    return parents[city]

def union_city(parents, check, a, b):
    check[a][b] = True
    check[b][a] = True

    root_a = find_parent(parents, a)
    root_b = find_parent(parents, b)

    if root_a == root_b:
        return
    
    if root_a < root_b:
        parents[root_a] = root_b
    else:
        parents[root_b] = root_a

def solution(board, plans):
    N = len(board)
    parents = [idx for idx in range(len(board))]
    check = [[False] * N for _ in range(N)] 

    for row in range(N):
        for col in range(N):        
            if check[row][col] or check[col][row]:
                continue
            if board[row][col] == 0:
                continue
            
            union_city(parents, check, row, col)
    
    # 여행을 갈 도시들이 전부 같은 집합이라면 => 가능한 계획
    answer = set([find_parent(parents, city) for city in plans])

    # 같은 집합
    if len(answer) == 1:
        print('YES')
    else:
        print('NO')
    return

CITY = int(input())
PLAN = int(input())

board = [list(map(int, input().split())) for _ in range(CITY)]
plans = list(map(int, input().split()))
plans = [city - 1 for city in plans]

solution(board, plans)