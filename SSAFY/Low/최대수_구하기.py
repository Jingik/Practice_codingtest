import math

T = int(input())

for i in range(1, T+1):
    case = list(map(int, input().split()))
    case = sorted(case)
    Max = max(case)
    print(f'#{i} {Max}')
