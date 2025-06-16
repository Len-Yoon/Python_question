## 예비 비교값
INF = 9999

# 최소 가중치 찾을시 값 교체
def choose_vertex(dist, found):
    min_val = INF # 아직 경로를 모름을 나타내는 임의의 큰 값
    minpos = -1
    for i in range(len(dist)):
        if dist[i] < min_val and not found[i]:
            min_val = dist[i]
            minpos = i # 방문안한 노드 중 가장 가까운 노드
    return minpos

#최단 경로 구하기 + 최단 경로 저장
def shortest_path_dijkstra(vtx, adj, start): #노드, 가중치, 시작점
    vsize = len(vtx) # 총 노드 A,B,C,D,E,F,G 길이 7
    dist = list(adj[start]) # 각 노드 최소 가중치 정보 리스트
    path = [start] * vsize # 경로 추적용
    found = [False] * vsize # 최단경로 확정 유무
    found[start] = True # 첫 스타트 자리 True로 초기화
    dist[start] = 0
    print(found)

    for i in range(vsize - 1):  # 시작점 제외, vsize-1번 반복
        print("Step%2d: " % (i+1), dist)
        u = choose_vertex(dist, found)
        found[u] = True
        for w in range(vsize):
            if not found[w]:
                if dist[u] + adj[u][w] < dist[w]:
                    dist[w] = dist[u] + adj[u][w]
                    path[w] = u # 이전 노드 기록
    return path

# 노드값
vertex = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
# 가중치
weight = [
    [0, 7, INF, INF, 3, 10, INF],
    [7, 0, 4, 10, 2, 6, INF],
    [INF, 4, 0, 2, INF, INF, INF],
    [INF, 10, 2, 0, 11, 9, 4],
    [3, 2, INF, 11, 0, 13, 5],
    [10, 6, INF, 9, 13, 0, INF],
    [INF, INF, INF, 4, 5, INF, 0]
]

print("Shortest Path By Dijkstra Algorithm")
start = 0
path = shortest_path_dijkstra(vertex, weight, start)

# 최단 경로 추가
for end in range(len(vertex)):
    if end != start:
        print("[최단경로: %s->%s] %s" % (vertex[start], vertex[end], vertex[end]), end='')
        temp = end
        while path[temp] != start:
            print(" <- %s" % vertex[path[temp]], end='')
            temp = path[temp]
        print(" <- %s" % vertex[path[temp]])
