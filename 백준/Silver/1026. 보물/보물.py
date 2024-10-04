import sys
input = sys.stdin.readline

# 1. 최소값이 되기 위해서는 sort 하고 서로 반대
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort()
total = 0
for i in range(N):
    total += A[i] * B[-i-1]

print(total)