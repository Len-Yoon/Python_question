# 무한대 값을 나타내는 상수 (연결되지 않은 노드 표시)
INF = 9999

# 가중치 인접 행렬 (None은 직접 연결 없음)
# 노드 순서: ['A', 'B', 'C', 'D', 'E', 'F', 'G']
weight = [
    [0, 7, None, None, 3, 10, None],
    [7, 0, 4, 10, 2, 6, None],
    [None, 4, 0, 2, None, None, None],
    [None, 10, 2, 0, 11, 9, 4],
    [3, 2, None, 11, 0, None, 5],
    [10, 6, None, 9, None, 0, None],
    [None, None, None, 4, 5, None, 0]
]

# 노드 이름 리스트
nodes = ['A', 'B', 'C', 'D', 'E', 'F', 'G']


def dijkstra(graph, start):
    """다익스트라 알고리즘 구현 함수"""
    n = len(graph)
    visited = [False] * n  # 방문 여부 추적
    dist = [INF] * n  # 시작점부터의 최단 거리
    dist[start] = 0  # 시작 노드 거리 0 초기화

    prev = [None] * n  # 최단 경로 추적을 위한 이전 노드 기록

    # 모든 노드 방문 시도
    for _ in range(n):
        # 미방문 노드 중 최소 거리 노드 선택
        u = -1
        min_dist = INF
        for i in range(n):
            if not visited[i] and dist[i] < min_dist:
                min_dist = dist[i]
                u = i

        if u == -1:  # 더 이상 방문할 노드 없을 때 종료
            break

        visited[u] = True  # 현재 노드 방문 처리

        # 인접 노드 거리 갱신
        for v in range(n):
            if graph[u][v] is not None and not visited[v]:
                # 더 짧은 경로 발견 시 갱신
                if dist[v] > dist[u] + graph[u][v]:
                    dist[v] = dist[u] + graph[u][v]
                    prev[v] = u  # 경로 추적을 위해 이전 노드 기록

    return dist, prev


def reconstruct_path(prev, start, end):
    """최단 경로 재구성 함수"""
    path = []
    at = end
    while at is not None:  # 시작 노드까지 역추적
        path.append(at)
        at = prev[at]
    path.reverse()  # 경로 순서 정방향으로 변경
    return path if path[0] == start else []  # 유효한 경로인지 확인


# 실행 코드
distances, prev_nodes = dijkstra(weight, 0)  # A 노드(인덱스 0)에서 시작

# 결과 출력
for i, d in enumerate(distances):
    path_indices = reconstruct_path(prev_nodes, 0, i)  # 경로 인덱스 추출
    path_nodes = [nodes[idx] for idx in path_indices]  # 노드 이름 변환
    print(f"dist(A, {nodes[i]}) = {d if d != INF else None}, path: {path_nodes}")
