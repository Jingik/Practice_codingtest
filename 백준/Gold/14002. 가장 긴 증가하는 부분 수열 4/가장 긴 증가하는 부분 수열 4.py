import sys
input = sys.stdin.readline

N = int(input())
input_array = list(map(int, input().split()))
dp = [1] * N

for i in range(N):
    for j in range(i):
        if input_array[i] > input_array[j]:
            dp[i] = max(dp[i], dp[j] + 1)
print(max(dp))

Sequence = []
order = max(dp) 
for i in range(N - 1, -1, -1):
    if dp[i] == order: 
        Sequence.append(input_array[i]) 
        order -= 1

Sequence.reverse()
print(*Sequence)