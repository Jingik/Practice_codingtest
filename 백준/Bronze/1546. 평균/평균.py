import sys

input =sys.stdin.readline
#
N = int(input())
List = list(map(int, input().split()))
Max = max(List)
New_List = 0
for i in range(N):
    New_List += List[i] / Max * 100
print(New_List/N)

