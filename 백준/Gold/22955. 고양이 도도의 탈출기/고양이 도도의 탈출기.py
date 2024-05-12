from heapq import heappop,heappush

def bfs():
    q=[]
    heappush(q,[0,sx,sy])
    visited[sx][sy]=0
    while q:
        cnt,x,y=heappop(q)
        if cnt>visited[x][y]:
            continue
        if room[x][y]=='E':
            print(visited[x][y])
            return
       #지금 일반 바닥에 있다면-->좌우+아래에 사다리있는지 살핀다
        if room[x][y]=='F':
            for d in range(2):
                nx=x+dx[d]
                ny=y+dy[d]

                if nx<0 or nx>=N or ny<0 or ny>=M:
                    continue

                if room[nx][ny]=='D':
                    continue

                if visited[nx][ny]>cnt+1:
                    visited[nx][ny]=cnt+1
                    heappush(q,[cnt+1,nx,ny])

            if x+1<N and room[x+1][y]=='L' and visited[x+1][y]>cnt+5:
                visited[x+1][y]=cnt+5
                heappush(q,[cnt+5,x+1,y])
        #지금 사다리구역이 왔다-->위로 올라거가나 좌우를 본다+아래 혹시나 사다리있으면 내려감
        elif room[x][y]=='L':
            for d in range(2):
                nx=x+dx[d]
                ny=y+dy[d]

                if nx<0 or nx>=N or ny<0 or ny>=M:
                    continue

                if room[nx][ny]=='D':
                    continue

                if visited[nx][ny]>cnt+1:
                    visited[nx][ny]=cnt+1
                    heappush(q,[cnt+1,nx,ny])

            if x-1>=0 and not room[x-1][y]=='D' and visited[x-1][y]>cnt+5:
                visited[x-1][y]=cnt+5
                heappush(q,[cnt+5,x-1,y])
            if x+1<N and room[x+1][y]=='L' and visited[x+1][y]>cnt+5:
                visited[x+1][y]=cnt+5
                heappush(q,[cnt+5,x+1,y])

        #지금있는 구역이 X-->계속 내려감.
        else:

            nx=room[x][y][0]
            ny=room[x][y][1]

            if visited[nx][ny]>cnt+10:
                visited[nx][ny]=cnt+10
                heappush(q,[cnt+10,nx,ny])

    print('dodo sad')
    return


dx=[0,0]
dy=[1,-1]
N,M=map(int,input().split())
room=[]
sx,sy=-1,-1

fall=[]
for x in range(N):
    tmp=list(input().rstrip())
    for y in range(M):
        if tmp[y]=='C':
            tmp[y]='F'
            sx,sy=x,y
        elif tmp[y]=='X':
            fall.append((x,y))
    room.append(tmp)
#떨어질 지점 전처리

for fx,fy in fall:
    #혹시 좌표가 넣은 지점이라면 스킵
    if room[fx][fy]!='X':
        continue
    tmp_fall=[]
    tmp_fall.append([fx,fy])
    nx=fx
    #내려가면서 만나는 X점들 모두 모아본다
    while True:
        nx+=1
        if room[nx][fy]!='X':
            break
        tmp_fall.append([nx,fy])
    #개를 만난다-->떨어지면 개를 무조건 만나는 거니 사실상 개가 있는 지점이라봐도 무방
    if room[nx][fy]=='D':
       for px,py in tmp_fall:
           room[px][py]='D'
    #정상적-->지나간 모든 좌표에 낙하지점 설정
    else:
        for px,py in tmp_fall:
            room[px][py]=[nx,fy]

visited=[[1e9]*M for _ in range(N)]
bfs()
