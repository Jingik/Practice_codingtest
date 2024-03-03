import sys
input = sys.stdin.readline

# 유니온 파인드
def find(x):
    if parent[x] < 0:
        return x
    
    parent[x] = find(parent[x])
    return parent[x]
    
def union(a, b):
    root_a = find(a)
    root_b = find(b)
    
    if root_a == root_b:
        return False
    
    if parent[root_a] < parent[root_b]:
        parent[root_b] = root_a
    elif parent[root_a] > parent[root_b]:
        parent[root_a] = root_b
    else:
        parent[root_a] = root_b
        parent[root_b] -= 1
    
    return True

# DFS에 활용할 제너레이터
def move(x, y, N, M):
    if N > 1:
        if 0 < x < N-1:
            yield (x-1, y)
            yield (x+1, y)
        elif x == 0:
            yield(x+1, y)
        else:
            yield(x-1, y)
    
    if M > 1:
        if 0 < y < M-1:
            yield (x, y-1)
            yield (x, y+1)
        elif y == 0:
            yield(x, y+1)
        else:
            yield(x, y-1)

# 섬마다 고유 번호를 주기 위한 DFS
# 값이 1인(=섬인) 모든 좌표에, 속한 섬의 번호와 그 좌표의 x, y 값을 튜플로 저장
def DFS(x, y, num, N, M):
    visited[x][y] = True
    island[-1].append((num, x, y))
    for adj_x, adj_y in move(x, y, N, M):
        if board[adj_x][adj_y] == 1 and visited[adj_x][adj_y] == False:
            DFS(adj_x, adj_y, num, N, M)

N, M = map(int, input().split())
board = []
for _ in range(N):
    board.append([*map(int, input().split())])

visited = [[False]*M for _ in range(N)]
edges = [] # MST 후보 간선들을 담을 리스트
island = [] # 섬 별로 좌표를 그룹핑한 리스트를 모아둔 리스트
num = 1 # 섬 번호
for row in range(N):
    for col in range(M):
        if board[row][col] == 1 and visited[row][col] == False:
            island.append([])
            DFS(row, col, num, N, M)
            num += 1

# MST 후보 간선을 찾는 작업
for n1 in range(len(island)-1): # n1번째 섬
    for n2 in range(n1 + 1, len(island)): # n2번째 섬
        candidates = [] # n1섬과 n2섬 사이의 모든 간선을 구해서 여기에 저장할거임
        for num1, x1, y1 in island[n1]: # n1섬 위의 좌표 한 점
            for num2, x2, y2 in island[n2]: # n2섬 위의 좌표 한 점
                if x1 == x2 and abs(y1 - y2) - 1 > 1: # x축 기준 동일선상에 있고, y값의 차의 절댓값이 2 이상이여야 함
                    # 만약 x축 기준 동일선상에서, 두 좌표 사이의 좌표들 중에 값이 1인게 있으면
                    # 이 두 좌표 사이에는 다리를 놓을 수 없음
                    if y1 < y2 and sum(board[x1][y1+1:y2]) > 0:
                        continue
                    elif y1 > y2 and sum(board[x1][y1-1:y2:-1]) > 0:
                        continue
                    candidates.append(abs(y1 - y2) - 1)
                if y1 == y2 and abs(x1 - x2) - 1 > 1:
                    if x1 < x2 and sum([board[nx][y1] for nx in range(x1+1, x2)]) > 0:
                        continue
                    elif x1 > x2 and sum([board[nx][y1] for nx in range(x1-1, x2, -1)]) > 0:
                        continue
                    candidates.append(abs(x1 - x2) - 1)
        if candidates:
            edges.append((min(candidates), n1 + 1, n2 + 1)) # n1섬과 n2섬 사이 간선 중 최소 가중치 간선을 MST 후보 간선으로 저장

# 크루스칼
edges.sort()
parent = [-1]*(len(island)+1)
res = 0
for w, x, y in edges:
    if union(x, y):
        res += w

# 만약 크루스칼 실행 후 모든 섬이 연결되어 있지 않다면 -1 출력
isMST = True
for i in range(1, len(island)):
    if find(i) != find(i+1):
        isMST = False

if isMST == False:
    print(-1)
else:
    print(res)