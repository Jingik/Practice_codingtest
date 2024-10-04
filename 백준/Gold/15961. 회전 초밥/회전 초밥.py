import sys
input = sys.stdin.readline

N, D, K, C = map(int, input().split())
belt = [int(input()) for _ in range(N)]

# 초밥 가짓수 
variety = [0] * (D + 1)
variety[C] = 1
# 무조건 쿠폰은 먹음
cnt = 1
result = 1

for k in range(K):
    if variety[belt[k]] == 0:
        cnt += 1
    
    variety[belt[k]] += 1

for n in range(N):
    result = max(result, cnt)

    variety[belt[n]] -= 1
    if variety[belt[n]] == 0:
        cnt -= 1
    
    if variety[belt[(n + K) % N]] == 0:
        cnt += 1
    variety[belt[(n + K) % N]] += 1

print(result)