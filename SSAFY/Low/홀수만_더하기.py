T = int(input())

for i in range(1, T+1):
    case = list(map(int, input().split()))
    Sum = 0
    for j in case:
        if (j % 2) == 1:
            Sum += j
        else:
            Sum += 0
            
    print(f'#{i} {Sum}')