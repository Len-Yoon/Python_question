INF = 9999  # Prim에서 무한대 대체

# --------- 유니온-파인드 (Disjoint Set) ---------
parent = []

def init_set(n):
    global parent
    parent = [i for i in range(n)]

def find(u):
    if parent[u] != u:
        parent[u] = find(parent[u])
    return parent[u]

def union(u, v):
    u_root = find(u)
    v_root = find(v)
    if u_root != v_root:
        parent[v_root] = u_root

# --------- Kruskal 알고리즘 ---------
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
    print("Kruskal MST 간선:")
    while edgeAccepted < vsize - 1 and eList:
        e = eList.pop(0)  # 가중치가 가장 작은 간선 선택
        uset = find(e[0])
        vset = find(e[1])
        if uset != vset:
            print("  (%s, %s, %d)" % (vertex[e[0]], vertex[e[1]], e[2]))
            union(uset, vset)
            mst_weight += e[2]
            edgeAccepted += 1
    print("Kruskal MST 가중치 합:", mst_weight)
    print()

# --------- Prim 알고리즘 ---------
def getMinVertex(dist, selected):
    minv = 0
    mindist = INF
    for v in range(len(dist)):
        if not selected[v] and dist[v] < mindist:
            mindist = dist[v]
            minv = v
    return minv

def MSTPrim(vertex, adj):
    vsize = len(vertex)
    dist = [INF] * vsize
    selected = [False] * vsize
    dist[0] = 0  # 시작 정점은 0번
    mst_weight = 0

    print("Prim MST 방문 순서 및 간선:")
    for i in range(vsize):
        u = getMinVertex(dist, selected)
        selected[u] = True
        print("  방문:", vertex[u])

        for v in range(vsize):
            if adj[u][v] is not None:
                if not selected[v] and adj[u][v] < dist[v]:
                    dist[v] = adj[u][v]
    # MST 가중치 합 계산 (dist 배열에는 각 노드가 트리에 추가될 때의 최소 비용이 저장됨)
    mst_weight = sum(dist)
    print("Prim MST 가중치 합:", mst_weight)
    print()

# --------- 그래프 데이터 ---------
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

# --------- 실행 ---------
MSTKruskal(vertex, adj)
MSTPrim(vertex, adj)
