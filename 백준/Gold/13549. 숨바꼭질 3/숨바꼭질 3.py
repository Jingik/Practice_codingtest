import sys
from collections import deque

input = sys.stdin.readline
 
a, b = map(int,input().split())

time = [0]*100001
 
def bfs(x,y):
    queue = deque()
    if x == 0 :
        queue.append(1)
    else :
        queue.append(x)
    
    while queue:
        x = queue.popleft()
        if y == x :
            return time[x]
        
        for nx in (x-1,x+1,x*2):
            if 0 <= nx < 100001 and time[nx]==0:
                if nx == 2*x :
                    time[nx] = time[x]
                    queue.appendleft(nx)
                else : 
                    time[nx] = time[x] + 1
                    queue.append(nx)
 
if a==0:
    if b==0:
        print(0)
    else:
        print(bfs(a,b)+1)
else :
    print(bfs(a,b))