import sys

def input():
    return sys.stdin.readline().strip()

A = int(input())
B = list(map(int,input().split()))

Arr = [0] * A

for i in range(1, A+1):
    k = B[i-1]
    cnt = 0
    for j in range(A):
        if cnt == k and Arr[j] == 0:
            Arr[j] = i
            break
        elif Arr[j] == 0:
            cnt += 1

print(*Arr)