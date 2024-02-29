import sys
input = sys.stdin.readline
N = int(input())
Count = list(map(int, input().split()))
Board = [i for i in range(1, N+1)]
final = []
for i in range(N):
    if i < 2:
        final.append(Board[i])
    else: 
        final.insert(Count[i],Board[i])
print(*final[::-1])