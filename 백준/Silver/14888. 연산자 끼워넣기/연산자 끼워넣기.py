n=int(input())
a=list(map(int,input().split()))
oper=list(map(int,input().split()))
result=[]

def dfs(cnt,p,minus,mul,d,now):
    if cnt==n-1:
        result.append(now)
        return

    if p<oper[0]:
        dfs(cnt+1,p+1,minus,mul,d,now+a[cnt+1])
    if minus<oper[1]:
        dfs(cnt+1,p,minus+1,mul,d,now-a[cnt+1])
    if mul<oper[2]:
        dfs(cnt+1,p,minus,mul+1,d,now*a[cnt+1])
    if d<oper[3]:
        if now<0:
            temp=(-now)//a[cnt+1]
            now=-temp
        else: now=now//a[cnt+1]
        dfs(cnt+1,p,minus,mul,d+1,now)

dfs(0,0,0,0,0,a[0])

print(max(result))
print(min(result))