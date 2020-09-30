parent  = {}
rank = {}

def find(vertex):
    # path compression 기법 적용
    if parent[vertex] != vertex:
        parent[vertex] = find(parent[vertex])
    return parent[vertex]

def union(vertex_a, vertex_b):
    root_a = find(vertex_a)
    root_b = find(vertex_b)

    # union-by-rank 기법 적용
    if rank[root_a] > rank[root_b]:
        parent[root_b] = root_a
    else :
        parent[root_a] = root_b
        if rank[root_a] == rank[root_b]:
            rank[root_b] += 1

def make_set(vertex):
    parent[vertex] = vertex
    rank[vertex] = 0

def kruskal(graph):
    mst = []

    # 1. 초기화 :: 정점들을 독립된 집합으로 선언
    for vertex in graph.get("vertices"):
        make_set(vertex)

    # 2. 가중치 기반 정렬
    edges = graph.get("edges")
    edges.sort()

    # 3. 간선 가중치 순서에 따라 반복하며,
    #    두 정점 연결 시 사이클이 되는 지 검사하고,
    #    사이클이 아닐 시 연결하는 작업
    for edge in edges:
        weight, vertex_a, vertex_b = edge
        if find(vertex_a) != find(vertex_b):
            union(vertex_a, vertex_b)
            mst.append(edge)

    return mst
            
mygraph = {
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

minimum_spanning_tree = kruskal(mygraph)
for i in minimum_spanning_tree:
    print(i)