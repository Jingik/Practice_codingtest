import sys

input = sys.stdin.readline

n = int(input().strip())
a = [[0, False] for _ in range(10)]
ans = 0

for _ in range(n):
    s = input().strip()
    m = 1
    a[ord(s[0]) - 65][1] = True
    for c in range(len(s) - 1, -1, -1):
        a[ord(s[c]) - 65][0] += m
        m *= 10

# 큰 값 순으로 정렬
a.sort(reverse=True, key=lambda x: x[0])

# 0에 할당되는 경우 방지
if a[9][1]:  # 만약 0이 반드시 할당되어야 하는 문자라면
    for i in range(8, -1, -1):
        if not a[i][1]:
            # 0 대신 다른 값 할당
            a.append(a.pop(i))
            break

# 최대 합 계산
for i in range(9):
    ans += a[i][0] * (9 - i)

print(ans)
