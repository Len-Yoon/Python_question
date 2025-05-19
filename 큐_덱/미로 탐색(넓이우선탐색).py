from collections import deque

# 미로 맵
map = [
    [1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 1],
    [1, 1, 1, 0, 0, 0],
    [1, 1, 1, 0, 1, 1],
    [1, 1, 1, 1, 1, 1],
]

map_size = 6 # 미로 크기
start = (1,0) # 시작 위치
end = (3,5) # 도착 위치
visited = [] # 방문 체크
directions = [(0, 1), (-1, 0), (0, -1), (1, 0)]  # 탐색 순서 (오른쪽->아래->왼쪽->위)

def find_map_load(map, map_size, start, end):
    # BFS 초기 설정
    visited = [[False for _ in range(map_size)] for _ in range(map_size)]  # 방문 기록 2차원 배열
    queue = deque([start])  # 큐 초기값(시작 위치)
    visited[start[0]][start[1]] = True  # 시작 위치 방문 처리
    parent = {start: None}  # 경로 복원을 위한 부모 노드 딕셔너리

    while queue:
        current = queue.popleft()  # 큐 맨 앞에서 요소 추출(FIFO)

        # 도착지 발견 시 경로 복원
        if current == end:
            path = []
            while current is not None:  # 부모 노드 역추적
                path.append(current)
                current = parent[current]
            return path[::-1]  # 역순 정렬(시작→도착 순으로)

        for dx, dy in directions:
            nx = current[0] + dx  # 다음 행 위치
            ny = current[1] + dy  # 다음 열 위치

            # 미방문 위치로 이동
            if (0 <= nx < map_size and 0 <= ny < map_size and map[nx][ny] == 0 and not visited[nx][ny]):
                queue.append((nx, ny))  # 큐에 다음 위치 추가
                visited[nx][ny] = True  # 다음 위치 방문 표시
                parent[(nx, ny)] = current  # 부모 노드 기록

    return -1

# 함수 실행
result = find_map_load(map, map_size, start, end)

# 결과 출력
if result != -1:
    print(f"경로: {result}")
else:
    print("경로 찾기 실패")