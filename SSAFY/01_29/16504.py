import sys
sys.stdin = open('./in.txt')

N = int(input())

for case in range(1, N+1):
    number = int(input())
    arr = list(map(int, input().split()))
    max_v = 0 # 가장 큰 낙차
    for i in range(number-1): # for i : 0 -> N-2, i 낙차를 구한 위치
        cnt = 0     # 오른쪽에 있는 더 낮은 높이의 개수
        for j in range(i+1, number): # for j : i+1 -> N-1
            if arr[i] > arr[j]:
                cnt += 1
                
        if max_v < cnt:
            max_v = cnt
    print(f'#{case} {max_v}')