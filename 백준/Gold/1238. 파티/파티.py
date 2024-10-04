import sys
import heapq

input = sys.stdin.readline

# 다익스트라 알고리즘을 이용해 최단 거리를 계산하는 함수
def dijkstra(start, N, graph):
    # 거리 테이블을 무한대로 초기화 (각 노드까지의 거리를 저장)
    dist = [float('inf')] * (N + 1)
    # 시작 노드의 거리는 0으로 설정
    dist[start] = 0
    # 우선순위 큐에 (현재까지의 거리, 현재 노드) 형태로 시작 노드를 추가
    pq = [(0, start)]
    
    # 우선순위 큐가 빌 때까지 반복
    while pq:
        # 가장 작은 거리를 가진 노드를 꺼냄 (현재까지의 거리, 현재 노드)
        current_time, current_node = heapq.heappop(pq)
        
        # 현재 노드까지의 거리가 이미 계산된 거리보다 크면 무시
        if current_time > dist[current_node]:
            continue
        
        # 현재 노드와 연결된 모든 이웃 노드를 확인
        for neighbor, travel_time in graph[current_node]:
            # 새로운 경로를 통해 이웃 노드까지의 거리를 계산
            new_time = current_time + travel_time
            # 새로 계산한 거리가 기존 거리보다 짧다면 업데이트
            if new_time < dist[neighbor]:
                dist[neighbor] = new_time
                # 우선순위 큐에 (새로운 거리, 이웃 노드) 추가
                heapq.heappush(pq, (new_time, neighbor))
    
    # 시작 노드로부터 각 노드까지의 최단 거리 배열 반환
    return dist

# 입력 처리
N, M, X = map(int, input().split())

# 그래프 초기화 (N+1개의 빈 리스트를 만듦, 인덱스는 1부터 N까지 사용)
graph = [[] for _ in range(N + 1)]
reverse_graph = [[] for _ in range(N + 1)]

# 주어진 도로 정보로 그래프 구성 (단방향 그래프)
for _ in range(M):
    st, ed, ti = map(int, input().split())
    # 출발지에서 도착지로 가는 길을 그래프에 추가
    graph[st].append((ed, ti))
    # 돌아오는 경로를 계산하기 위해 역방향 그래프에도 추가
    reverse_graph[ed].append((st, ti))

# 모든 노드에서 X로 가는 최단 거리를 계산 (역방향 그래프 사용)
dist_to_X = dijkstra(X, N, reverse_graph)

# X에서 모든 노드로 가는 최단 거리를 계산
dist_from_X = dijkstra(X, N, graph)

# 왕복 시간이 가장 긴 학생의 시간을 계산
max_time = 0
for i in range(1, N + 1):
    # 학생이 X까지 가는 거리와 돌아오는 거리가 모두 존재할 때
    if dist_from_X[i] != float('inf') and dist_to_X[i] != float('inf'):
        # 왕복 시간 계산
        round_trip_time = dist_from_X[i] + dist_to_X[i]
        # 가장 큰 왕복 시간을 저장
        max_time = max(max_time, round_trip_time)

# 가장 오래 걸린 학생의 왕복 시간을 출력
print(max_time)
