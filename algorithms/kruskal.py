# Kruskal's algorithm
# O(ElogE)
# => edges에 대해 sorting

# 입력 받은 node의 root 노드 찾는 함수
def find(parents, node):
    # path compression
    if parents[node] != node:
        parents[node] = find(parents, parents[node])

    return parents[node]


# 주어진 노드 트리를 하나의 트리로 합치는 함수
def union(parents, ranks, node1, node2):
    root1 = find(parents, parents[node1])
    root2 = find(parents, parents[node2])

    # union-by-rank
    # 두 트리의 높이가 다를 경우
    if ranks[root1] < ranks[root2]:
        parents[root1] = root2
    else:
        parents[root2] = root1
        # 두 트리의 높이가 같을 경우
        if ranks[root1] == ranks[root2]:
            ranks[root1] += 1
    return


def kruskal(graph):
    parents = dict()
    ranks = dict()
    mst = []

    # 1. 초기화
    for node in graph['vertices']:
        parents[node] = node
        ranks[node] = 0

    # 2. Edge 소팅 (오름차순)
    edges = graph['edges']
    edges.sort()

    # 3. union-find를 활용하여 mst 찾기
    for edge in edges:
        cost, node1, node2 = edge
        if find(parents, node1) != find(parents, node2):
            union(parents, ranks, node1, node2)
            print(parents, ranks)
            mst.append(edge)

    return mst


graph = {
    'vertices': ['A', 'B', 'C', 'D', 'E', 'F', 'G'],
    'edges': [
        (7, 'A', 'B'),
        (5, 'A', 'D'),
        (7, 'B', 'A'),
        (8, 'B', 'C'),
        (9, 'B', 'D'),
        (7, 'B', 'E'),
        (8, 'C', 'B'),
        (5, 'C', 'E'),
        (5, 'D', 'A'),
        (9, 'D', 'B'),
        (7, 'D', 'E'),
        (6, 'D', 'F'),
        (7, 'E', 'B'),
        (5, 'E', 'C'),
        (7, 'E', 'D'),
        (8, 'E', 'F'),
        (9, 'E', 'G'),
        (6, 'F', 'D'),
        (8, 'F', 'E'),
        (11, 'F', 'G'),
        (9, 'G', 'E'),
        (11, 'G', 'F')
    ]
}


kruskal(graph)
# [(5, 'A', 'D'), (5, 'C', 'E'), (6, 'D', 'F'), (7, 'A', 'B'), (7, 'B', 'E'), (9, 'E', 'G')]
