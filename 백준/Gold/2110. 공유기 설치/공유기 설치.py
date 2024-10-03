import sys
input = sys.stdin.readline

N, C = map(int, input().split())
stack = []

for _ in range(N):
    num = int(input())
    stack.append(num)

stack = sorted(stack) 
start = 1
end = stack[-1] - stack[0] 
answer = 0

while start <= end:
    mid = (start + end) // 2 
    count = 1  
    last_router = stack[0]  
    

    for i in range(1, N):
        if stack[i] - last_router >= mid: 
            count += 1 
            last_router = stack[i]
    
    if count >= C:
        answer = mid
        start = mid + 1
    else:
        end = mid - 1

print(answer)
