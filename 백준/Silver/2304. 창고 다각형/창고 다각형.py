import sys
input = sys.stdin.readline

N = int(input())
heights = [0] * 1001
Max_height = 0
Max_Index = 0
result = 0
for _ in range(N):
    Index, height = map(int, input().split())
    heights[Index] = height
    if Max_height <= height:
        Max_height = height
        Max_Index = Index
total_area = 0
high_area = 0
for i in range(Max_Index + 1):
    high_area = max(high_area, heights[i])
    total_area += high_area

high_area = 0
for i in range(1000, Max_Index, -1):
    high_area = max(high_area, heights[i])
    total_area += high_area

print(total_area)  # 총 면적 출력    