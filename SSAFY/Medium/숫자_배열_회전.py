T = int(input())

for t in range(1, T + 1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    result = [[0] * 3 for _ in range(N)]
    n = 0

    for _ in range(3):
        rotated = [[0] * N for _ in range(N)]
        for i in range(N):
            for j in range(N):
                rotated[i][j] = matrix[(N - 1) - j][i]

        matrix = rotated

        for idx, chars in enumerate(matrix):
            result[idx][n] = ''.join(map(str, chars))

        n = n + 1

    print(f'#{t}')

    for row in result:
        print(*row)