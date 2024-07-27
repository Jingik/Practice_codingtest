import sys
input = sys.stdin.readline

N = int(input())
num = sorted([int(input()) for _ in range(N)])
re_num = []

for i in range(1, N):
    re_num.append(num[i] - num[i-1])

def GCD(a, b):
    num = b
    div = a
    rest = num % div
    while rest != 0:
        num = div
        div = rest
        rest = num % div
    return div

gcd = re_num[0]
for idx in range(1, len(re_num)):
    gcd = GCD(gcd, re_num[idx])

result = set()
for i in range(2, int(gcd**0.5) + 1):
    if gcd % i == 0:
        result.add(i)
        result.add(gcd // i)
result.add(gcd)
print(*sorted(list(result)))