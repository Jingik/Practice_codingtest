def make_arr(k, n, m):
    if k == m:
        print(' '.join(map(str, arr)))
        return
    for i in range(len(visited)):
        if not visited[i]:
            visited[i] = True
            arr.append(i+1)
            make_arr(k+1, n, m)
            visited[i] = False
            arr.pop()

n,m = list(map(int, input().split()))
visited = [False for _ in range(n)]
arr = []
make_arr(0, n, m)