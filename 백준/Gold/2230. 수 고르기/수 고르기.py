import sys
input = sys.stdin.readline

# 수열 중 두 개를 골라서 그 차이가 가장 작은 값 찾아오기

N, M = map(int, input().split())
List = [int(input()) for _ in range(N)]
List.sort()

left, right = 0, 1
Min_de = float('inf')
while right < N:
    current = List[right] - List[left]
    if current >= M :
        Min_de = min(current, Min_de)
        left += 1
        if left == right:
            right += 1
    else:
        right += 1

print(Min_de)