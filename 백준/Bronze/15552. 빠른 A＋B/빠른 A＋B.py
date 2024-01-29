import sys
def input():
    return sys.stdin.readline()

T = int(input())
for _ in range(T):
    List = list(map(int, input().split()))
    print(sum(List))