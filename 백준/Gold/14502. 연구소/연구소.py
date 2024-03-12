from collections import deque
import math
from itertools import combinations
import copy
n,m=map(int,input().split())
a,blank,virus=[],[],[]
dy,dx=[1,-1,0,0],[0,0,1,-1]
for y in range(n):
    tmp=list(map(int,input().split()))
    a.append(tmp)
    for x in range(len(tmp)):
        if tmp[x]==0:
            blank.append((y,x))
        elif tmp[x]==2:
            virus.append((y,x))

allcase=combinations(blank,3)
def spread_virus(case):
    b=copy.deepcopy(a)
    q=deque()
    vis=[[0]*m for _ in range(n)]
    for y,x in virus:
        q.append((y,x))
        vis[y][x]=1
    for y,x in case:
        b[y][x]=1
    cnt=0
    while q:
        ll=len(q)
        for _ in range(ll):
            y,x=q.popleft()
            for i in range(4):
                yy=y+dy[i]
                xx=x+dx[i]
                if xx<0 or yy<0 or xx>=m or yy>=n: continue
                if vis[yy][xx]: continue

                if b[yy][xx]==0:
                    q.append((yy,xx))
                    vis[yy][xx]=1
                    b[yy][xx]=2
                    cnt+=1

    return len(blank)-3-cnt



answer=0
for case in allcase:
    tmp=spread_virus(list(case))
    if answer<tmp: answer=tmp

print(answer)