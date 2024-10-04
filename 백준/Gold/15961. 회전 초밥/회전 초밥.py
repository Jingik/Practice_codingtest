import sys
input = sys.stdin.readline

N, d, k, c = map(int, input().split())
belt = [int(input()) for _ in range(N)]

count = [0] * (d + 1) 
total = 0 
variety = 0 

for i in range(k):
    if count[belt[i]] == 0: 
        variety += 1
    count[belt[i]] += 1

total = variety
if count[c] == 0:
    total += 1

for i in range(1, N):

    outgoing_sushi = belt[i - 1]
    count[outgoing_sushi] -= 1
    if count[outgoing_sushi] == 0: 
        variety -= 1
        
    incoming_sushi = belt[(i + k - 1) % N]
    if count[incoming_sushi] == 0:
        variety += 1
    count[incoming_sushi] += 1
    current_total = variety
    if count[c] == 0: 
        current_total += 1
    total = max(total, current_total)

print(total)
