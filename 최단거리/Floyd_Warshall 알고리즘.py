def floyd_warshall(vertex, adj):
    INF = float('inf')
    vsize = len(vertex)

    # 거리 행렬 초기화 (None → INF 변환)
    dist = [[INF if adj[i][j] is None else adj[i][j]
             for j in range(vsize)] for i in range(vsize)]

    # 자기 자신으로의 거리 0 설정
    for i in range(vsize):
        dist[i][i] = 0

    # 플로이드-워셜 알고리즘 적용
    for k in range(vsize):
        for i in range(vsize):
            for j in range(vsize):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    # 결과 출력 함수
    def print_matrix(matrix):
        print("최단 거리 행렬:")
        print("\t" + "\t".join(vertex))
        for i in range(vsize):
            row = []
            for j in range(vsize):
                if matrix[i][j] == INF:
                    row.append("INF")
                else:
                    row.append(str(matrix[i][j]))
            print(vertex[i] + "\t" + "\t".join(row))

    print_matrix(dist)


# 주어진 그래프 데이터
weight = [
    [0, 7, None, None, 3, 10, None],
    [7, 0, 4, 10, 2, 6, None],
    [None, 4, 0, 2, None, None, None],
    [None, 10, 2, 0, 11, 9, 4],
    [3, 2, None, 11, 0, None, 5],
    [10, 6, None, 9, None, 0, None],
    [None, None, None, 4, 5, None, 0]
]
vertex = ['A', 'B', 'C', 'D', 'E', 'F', 'G']

# 알고리즘 실행
floyd_warshall(vertex, weight)
