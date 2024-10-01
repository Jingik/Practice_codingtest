def dfs(v, table, visited, path):
    visited[v] = True
    path.append(v)
    
    next_v = table[v]  # 다음 이동할 노드
    if not visited[next_v]:
        return dfs(next_v, table, visited, path)
    elif next_v in path:  # 사이클 발견
        return path[path.index(next_v):]  # 사이클 부분만 반환
    else:
        return []

# 입력 처리
N = int(input())  # N 값 입력
table = [0]  # 첫째 줄의 숫자들은 1부터 시작하므로 index 맞추기 위해 0 추가
for _ in range(N):
    table.append(int(input()))  # 둘째 줄의 숫자들 입력

visited = [False] * (N + 1)
result = []

# 모든 노드에 대해 DFS 실행
for i in range(1, N + 1):
    if not visited[i]:
        cycle = dfs(i, table, visited, [])
        result.extend(cycle)

# 결과 출력
result = sorted(set(result))  # 중복된 값 제거 후 정렬
print(len(result))  # 뽑힌 정수의 개수 출력
for num in result:
    print(num)  # 뽑힌 정수들 출력
