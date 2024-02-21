n=int(input())
a,b=map(int,input().split())
m=int(input())
arr=[[] for _ in range(n+1)]
chk=[False]*(n+1)
res=[]
for _ in range(m):
    x,y=map(int,input().split())
    arr[x].append(y)
    arr[y].append(x)
def dfs(v,num):
    num+=1
    chk[v]=True
    if v==b:
        res.append(num)
    for i in arr[v]:
        if chk[i]==False:
            dfs(i,num)

dfs(a,0)
if len(res)==0:
    print(-1)
else:
    print(res[0]-1)