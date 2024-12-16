import sys
input = sys.stdin.readline
n = int(input())
ratio = [[] for _ in range(n)]
mass = [0] * (n)
visited = [False] * n

def gcd(a,b):
  if a%b == 0:
    return b
  return gcd(b,a%b)

common_multi = 1
for _ in range(n-1):
  a, b, p, q = map(int,input().split())
  ratio[a].append((b,p,q))
  ratio[b].append((a,q,p))
  common_multi *= ((p*q)//gcd(p,q))
mass[0] = common_multi

def DFS(r):
  visited[r] = True
  for i in ratio[r]:
    if not visited[i[0]]:
      mass[i[0]] = i[2] * mass[r] // i[1]
      DFS(i[0])

DFS(0)

greatest_common_divisor = mass[0]
for i in range(n):
  greatest_common_divisor = gcd(greatest_common_divisor,mass[i])

for i in range(len(mass)):
  mass[i] = mass[i] // greatest_common_divisor
print(*mass)