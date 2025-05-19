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
    visited = [[False for _ in range(map_size)] for _ in range(map_size)]
    stack = [start] #DFS 시작 위치
    load = [start] #이동 경로 저장
    visited[start[0]][start[1]] = True # 방문 표시

    while stack:
        current = stack[-1] #현재 위치

        if current == end: 
            return load

        moved = False # 이동 여부 확인
        for dx, dy in directions:
            nx = current[0] + dx # 다음 위치 행
            ny = current[1] + dy # 다음 위치 열

            # 미방문 위치로 이동
            if (0 <= nx < map_size and 0 <= ny < map_size and map[nx][ny] == 0 and not visited[nx][ny]):
                stack.append((nx, ny)) # 스택에 다음 위치 추가
                load.append((nx, ny))  # 경로에 다음 위치 추가
                visited[nx][ny] = True # 다음 위치 방문 표시
                moved = True # 이동 성공
                break #이동 후 탈출

        # 이동 불가 상황
        if not moved:
            stack.pop() # 현재 위치 제거
            if stack: 
                load.append(stack[-1]) # 이동 불가 시 한 칸 되돌아 가도록 

    return -1  

# 함수 실행
result = find_map_load(map, map_size, start, end)

# 결과 출력
if result != -1:
    print(f"경로: {result}")
else:
    print("경로 찾기 실패")