# 불이 켜진 길로만 왕래가 가능하다
# 절약할 수 있는 최대 값 (DFS)
# 길의 가로등을 켜두면 거리수만큼 돈이 들어간다 | 소등한 만큼 돈을 아낄수 있다
# 양방향

### 필요변수
# m, n = 집의수, 길의 수
# road_list = (x번집, y번집, 거리)
# end = 00개가 주어짐

### 필요함수
# 크루스칼 알고리즘
# 각 그래프를 만들 형태

import sys
input = sys.stdin.readline

# 유니온 파인드를 위한 부모 테이블 초기화
def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, rank, x, y):
    root_x = find(parent, x)
    root_y = find(parent, y)
    if root_x != root_y:
        if rank[root_x] > rank[root_y]:
            parent[root_y] = root_x
        elif rank[root_x] < rank[root_y]:
            parent[root_x] = root_y
        else:
            parent[root_y] = root_x
            rank[root_x] += 1

while True:
    m, n = map(int, input().split())
    if m == 0 and n == 0:
        break

    road_list = []
    total_cost = 0

    for _ in range(n):
        x, y, length = map(int, input().split())
        road_list.append((length, x, y))
        total_cost += length

    # 크루스칼 알고리즘을 위해 정렬
    road_list.sort()

    # 유니온 파인드 초기화
    parent = [i for i in range(m)]
    rank = [0] * m

    min_cost = 0

    for length, x, y in road_list:
        if find(parent, x) != find(parent, y):
            union(parent, rank, x, y)
            min_cost += length

    # 절약할 수 있는 최대 비용 계산
    print(total_cost - min_cost)