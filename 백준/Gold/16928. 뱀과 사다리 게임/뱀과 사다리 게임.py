N, M = map(int, input().split())
board = [i for i in range(101)] + [1] * 5

for _ in range(N + M):
    start, end = map(int, input().split())
    board[start] = end

visited = [False, True] + [False] * 99
q = [1]
cnt = 0

while not visited[100]:
    nq = []
    cnt += 1

    for n in q:
        for i in range(1, 7):
            next = board[n + i]

            if not visited[next]:
                visited[next] = True
                nq.append(next)

    q = nq

print(cnt)