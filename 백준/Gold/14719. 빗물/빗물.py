import sys
input = sys.stdin.readline

def isvalid(i, j, H, W):
    if 0 <= j < H and 0 <= i < W:
        return True

H, W = map(int, input().split())
List = list(map(int,input().split()))
Map = [[0]*W for _ in range(H)]

for i in range(W):
    if List[i] > 0:
        for j in range(List[i]):
            Map[j][i] = 1
Total = 0
for j in range(H):
    number = 0
    for i in range(W):
        if Map[j][i] == 1 and isvalid(i+1, j, H, W) and Map[j][i+1] == 0:
            number += 1
        elif Map[j][i] == 0 and isvalid(i+1, j, H, W) and Map[j][i+1] == 1:
            Total += number
            number = 0
        elif number > 0 and Map[j][i] == 0 and isvalid(i+1, j, H, W) and Map[j][i+1] == 0:
            number += 1 
        elif number > 0 and Map[j][i] == 0 and isvalid(i+1, j, H, W) and Map[j][i+1] == 1:
            Total += number
            number = 0
        else:
            number = 0
            
print(Total)