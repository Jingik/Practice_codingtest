# 첫 째 줄에는 드래곤 커브의 개수
# 둘째줄 부터는 x y d g로 주어진다 g: 세대
# d -> 0 : (0, 1), 1 : (-1, 0), 2 : (0, -1), 3 : (1, 0)
# g -> 0 : (0,0) ~ (1,0) | 1 : (0, 0) - (1, 0) - (1, -1)
## 시계방향으로 90도 회전시킨 다음 커브 끝점에 붙인거 -> 현재 길이를 90도 회전 시키고 붙인거다
# g -> 2 : (0,0) ~ (1, 0) ~ (1, -1) ~ (0, -1) ~ (0, -2) 90도 회전 2번
# 3 -> 90 도 회전 4번

import sys
input = sys.stdin.readline

n = int(input())

Dircetion = [(0, 1), (-1, 0), (0, -1), (1, 0)]
graph = [[0] * 101 for _ in range(101)]

for _ in range(n):
    y, x, d, g = map(int, input().split())
    graph[x][y] = 1
    curve = [d]
    # len(curve) ^
    for _ in range(g):
        for i in range(len(curve)-1, -1, -1):
            curve.append((curve[i] + 1) % 4)
    
    for i in range(len(curve)):
        x += Dircetion[curve[i]][0]
        y += Dircetion[curve[i]][1]
        if  x < 0 or x > 100 or y < 0 or y > 100 :
            continue
        graph[x][y] = 1

answer = 0
for x in range(100):
    for y in range(100):
        if graph[x][y] == 1 and graph[x][y + 1] == 1 and graph[x + 1][y] == 1 and graph[x+1][y+1] == 1:
            answer += 1
            
print(answer)