import sys

def dfs(T):
    if T==S:
        print(1)
        sys.exit()
    if len(T)==0:
        return 0
    if T[-1]=='A':
        dfs(T[:-1]) 
    if T[0]=='B': 
        dfs(T[1:][::-1])

S = list(input())
T = list(input())
dfs(T)
print(0)