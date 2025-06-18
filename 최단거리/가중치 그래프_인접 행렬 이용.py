# 인접 행렬로 그래프를 표현 (가중치가 없는 곳은 None)
weight = [
    [0, 29, None, None, None, 10, None],
    [29, 0, 16, None, None, None, 15],
    [None, 16, 0, 12, None, None, None],
    [None, None, 12, 0, 22, None, 18],
    [None, None, None, 22, 0, 27, 25],
    [10, None, None, None, 27, 0, None],
    [None, 15, None, 18, 25, None, 0]
]

# 정점 리스트
vertex = ['A', 'B', 'C', 'D', 'E', 'F', 'G']

# 그래프를 (정점, 가중치 행렬)로 묶음
graph = (vertex, weight)

# 그래프의 모든 간선 가중치의 합을 구하는 함수
def weightSum(vlist, W):
    sum = 0
    # 모든 정점 쌍에 대해
    for i in range(len(vlist)):
        for j in range(i+1, len(vlist)):  # 중복 방지 (무방향 그래프)
            if W[i][j] != None:           # 간선이 존재하면
                sum += W[i][j]            # 가중치 합산
    return sum  # <-- return의 들여쓰기 오류 수정

# 전체 간선 가중치 합 출력
print('AM : weight sum = ', weightSum(vertex, weight))

# 그래프의 모든 간선을 출력하는 함수
def printAllEdges(vlist, W):
    for i in range(len(vlist)):
        for j in range(i+1, len(W[i])):  # 중복 방지 (무방향 그래프)
            if W[i][j] != None and W[i][j] != 0:  # 간선이 존재하고 자기 자신이 아닐 때
                # (정점1, 정점2, 가중치) 형태로 출력
                print("(%s,%s,%d)" % (vlist[i], vlist[j], W[i][j]), end=' ')
    print()  # 줄 바꿈

# 모든 간선 출력
printAllEdges(vertex, weight)
