import sys
input = sys.stdin.readline

def rotate_belt(A, robots, N):
    A = [A[-1]] + A[:-1]  
    robots = [0] + robots[:-1]  
    robots[N-1] = 0  
    return A, robots

def move_robots(A, robots, N):
    for i in range(N-2, -1, -1):
        if robots[i] == 1 and robots[i+1] == 0 and A[i+1] > 0: 
            robots[i] = 0
            robots[i+1] = 1
            A[i+1] -= 1  
    robots[N-1] = 0 
    return A, robots

def put_robot(A, robots):
    if A[0] > 0: 
        robots[0] = 1
        A[0] -= 1 
    return A, robots

def count_zero(A):
    return A.count(0)

N, K = map(int, input().split())
A = list(map(int, input().split()))
robots = [0] * N
steps = 0

while count_zero(A) < K:
    steps += 1
    A, robots = rotate_belt(A, robots, N)
    A, robots = move_robots(A, robots, N)
    A, robots = put_robot(A, robots)

print(steps)
