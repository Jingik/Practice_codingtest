# 1. 첫 째 줄에 사건의 개수 : n , 알고있는 사건의 갯수 : k
# 2. k 줄에는 사건의 관계를 알 고 있는 두 사건의 번호
# 사건의 번호는 1보다 크거나 같고 N 보다 작거나 같은 자연수
# print 앞에 있는 번호의 사건이 먼저 일어 났으면 -1, 모르겟으면 0, 뒤에있는 번호 사건이 먼저 일어났으면 1
# k 개가 주어지는데 이는 앞에 있는 사건이 뒤에 있는 번호보다 먼저 일어났음을 의미

### 필요 변수
# n, k : n개의 사건의 개수, 사건의 전후 갯수
# appoint : 조건 dp -> n + 1만큼의 리스트 -> 내가 무조건 앞 서는거 저장
# 대신 확인 할 때 해당 변수 안에도 그 수가 있다면 그 수도 포함해서 저장
# t : 테스트 갯수
# check : set으로 중복 방지
import sys # 개선
ip = sys.stdin.readline # 개선

n, k = map(int, ip().split()) # 개선
arr = [[0] * (n + 1) for _ in range(n + 1)] # 개선 (maxsize to 0)

for _ in range(k):
    a, b = map(int, ip().split()) # 개선
    arr[a][b] = 1

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if arr[i][k] + arr[k][j] == 2:
                arr[i][j] = 1


s = int(input())
for _ in range(s):
    x, y = map(int, ip().split()) # 개선
    if arr[x][y] == 1:
        print(-1)
    elif arr[y][x] == 1:
        print(1)
    else:
        print(0)