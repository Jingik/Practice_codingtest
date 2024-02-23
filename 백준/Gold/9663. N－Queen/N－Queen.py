import sys
input = sys.stdin.readline

n = int(input())

def promising(row):
    for before_row in range(row):
        # 같은 열 or 같은 대각선 상에 있는 경우
        if(graph_col[before_row] == graph_col[row] or 
           abs(graph_col[before_row]-graph_col[row])==abs(before_row-row)):
            return False
    return True

result = 0
graph_col = [0] * n 
def dfs(row):
    global result
    if row == n:
        result += 1
    else:
        for i in range(n):
            # Queen 놓기
            graph_col[row] = i
            if promising(row):
                dfs(row+1)

dfs(0)
print(result)