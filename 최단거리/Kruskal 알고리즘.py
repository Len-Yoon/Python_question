# 유니온-파인드(Disjoint Set) 구현
parent = []

def init_set(n):
    global parent
    parent = [i for i in range(n)]

def find(u):
    if parent[u] != u:
        parent[u] = find(parent[u])  # 경로 압축
    return parent[u]

def union(u, v):
    u_root = find(u)
    v_root = find(v)
    if u_root != v_root:
        parent[v_root] = u_root

# 크루스칼 알고리즘
def MSTKruskal(vertex, adj):
    vsize = len(vertex)
    init_set(vsize)
    eList = []

    # 모든 간선 정보를 리스트에 저장 (중복 방지: i < j)
    for i in range(vsize - 1):
        for j in range(i + 1, vsize):
            if adj[i][j] is not None:
                eList.append((i, j, adj[i][j]))

    # 가중치 기준 오름차순 정렬
    eList.sort(key=lambda e: e[2])

    edgeAccepted = 0
    mst_weight = 0
    print("MST Kruskal 결과 간선:")
    while edgeAccepted < vsize - 1 and eList:
        e = eList.pop(0)  # 가중치가 가장 작은 간선 선택
        uset = find(e[0])
        vset = find(e[1])
        if uset != vset:
            print("  (%s, %s, %d)" % (vertex[e[0]], vertex[e[1]], e[2]))
            union(uset, vset)
            mst_weight += e[2]
            edgeAccepted += 1
    print("최소 신장 트리 가중치 합:", mst_weight)

# 예시 데이터
vertex = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
adj = [
    [0, 29, None, None, None, 10, None],
    [29, 0, 16, None, None, None, 15],
    [None, 16, 0, 12, None, None, None],
    [None, None, 12, 0, 22, None, 18],
    [None, None, None, 22, 0, 27, 25],
    [10, None, None, None, 27, 0, None],
    [None, 15, None, 18, 25, None, 0]
]

MSTKruskal(vertex, adj)
