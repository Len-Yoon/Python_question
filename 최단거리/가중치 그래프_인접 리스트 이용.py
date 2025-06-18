# 인접 리스트로 그래프 표현 (각 정점: { (이웃, 가중치), ... } )
graphAL = {
    'A': set([('B', 29), ('F', 10)]),
    'B': set([('A', 29), ('C', 16), ('G', 15)]),
    'C': set([('B', 16), ('D', 12)]),
    'D': set([('C', 12), ('E', 22), ('G', 18)]),
    'E': set([('D', 22), ('F', 27), ('G', 25)]),
    'F': set([('A', 10), ('E', 27)]),
    'G': set([('B', 15), ('D', 18), ('E', 25)])
}

# 전체 간선 가중치의 합을 구하는 함수
def weightSum(graph):
    sum = 0
    for v in graph:
        for e in graph[v]:
            sum += e[1]  # e[1]이 가중치
    return sum // 2  # 무방향 그래프이므로 2로 나눔

print('AL : weight sum = ', weightSum(graphAL))

# 모든 간선을 출력하는 함수
def printAllEdges(graph):
    for v in graph:
        for e in graph[v]:
            print("(%s,%s,%d)" % (v, e[0], e[1]), end=' ')
    print()

printAllEdges(graphAL)
