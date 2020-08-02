# 네트워크
# https://programmers.co.kr/learn/courses/30/lessons/43162


from collections import deque


# 방법1 - BFS 풀이
def bfs(n, computers, check, queue):
    while queue:
        node = queue.popleft()

        for adjacent in range(n):
            if computers[node][adjacent] and check[adjacent] == False:
                queue.append(adjacent)
                check[adjacent] = True    
    return


# 방법 1 - BFS
def solution1(n, computers):
    answer = 0
    check = [False] * n
    queue = deque()

    # 모든 노드에 대해서
    for i in range(n):
        # 방문 안한 노드가 있다면 => BFS => 네트워크 + 1
        if check[i] == False:
            queue.append(i)

            bfs(n, computers, check, queue)
            answer += 1


    return answer


# 방법 2 - DFS 풀이
def dfs(n, computers, check, i):
    check[i] = True # 현재 방문한 지점 체크

    for adjacent in range(n):
        if computers[i][adjacent] and check[adjacent] == False:
            dfs(n, computers, check, adjacent)
    return


# 방법 2 - DFS
def solution2(n, computers):
    answer = 0
    check = [False] * n

    # 모든 노드에 대해서
    for i in range(n):
        # 방문 안한 노드에 대해서 탐색 => DFS
        if check[i] == False:
            dfs(n, computers, check, i)
            answer += 1

    return answer


# 방법 3 - FIND
def find_parent(parents, me):
    # 부모 노드가 자신인 경우
    if parents[me] == me:
        return me
    # 부모 노드가 자신이 아닌 경우
    else:
        parents[me] = find_parent(parents, parents[me]) # 부모 노드 업데이트
        return parents[me] # 업데이트 된 부모노드 반환

# 방법 3 - UNION
def union_set(parents, ranks, node1, node2):
    root1 = find_parent(parents, node1)
    root2 = find_parent(parents, node2)

    if root1 == root2:
        return

    # 부모 노드의 rank 값을 비교해 => 부모 노드, rank 업데이트
    if ranks[root1] == ranks[root2]:
        parents[root1] = root2
        ranks[root2] += 1

    else:
        if ranks[root1] < ranks[root2]:
            parents[root1] = root2
        else:
            parents[root2] = root1
    
    return
        

# 방법 3 - Union Find ** 아직 익숙지 않음
def solution3(n, computers):
    answer = 0
    parents = [node for node in range(n)] # 부모 노드 집합
    ranks = [0] * n # 트리의 height를 나타낼 리스트

    for start in range(n):
        for end in range(n):
            if start == end:
                continue
            # 연결 되어있는 노드들에 대해서
            if computers[start][end]:
                # union-find 진행
                union_set(parents, ranks, start, end)

    for node in range(n):
        if node == find_parent(parents, node):
            answer += 1

    return answer


n = 3
computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]	
print(solution1(n, computers))
print(solution2(n, computers))
print(solution3(n, computers))