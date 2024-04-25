import sys
input = sys.stdin.readline 
N = int(input())
data = list(map(lambda x: int(x) if x.isdigit() else x, input()))
result = -int(1e9)


def calculate(num1, num2, s): 
    if s == '+':
        return num1 + num2
    elif s == '-':
        return num1 - num2
    elif s == '*':
        return num1 * num2

def Dfs(lev, pre_sum):
    global result
    if lev >= N:  
        result = max(result, pre_sum)  
        return
    if lev + 3 < N: 
        Dfs(lev + 4, calculate(pre_sum, calculate(data[lev + 1], data[lev + 3], data[lev + 2]), data[lev]))
        
    Dfs(lev + 2, calculate(pre_sum, data[lev + 1], data[lev]))  

if N == 1:  
    result = data[0]
else:
    Dfs(1, data[0])

print(result)