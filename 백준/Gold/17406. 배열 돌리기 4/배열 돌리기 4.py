from itertools import permutations
from copy import deepcopy

N, M, K = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(N)]
rcs = [list(map(int, input().split())) for _ in range(K)]

ans = 987654321

# 1. 회전 순서 정하기 (최대 6!=720)
for p in permutations(rcs, K):
    # 2. 회전
    copy_a = deepcopy(a)  # 원본리스트 카피
    for r, c, s in p:
        r -= 1
        c -= 1
        for n in range(s, 0, -1):
            tmp = copy_a[r-n][c+n]
            copy_a[r-n][c-n+1:c+n+1] = copy_a[r-n][c-n:c+n]  # ->
            for row in range(r-n, r+n):  # ↑
                copy_a[row][c-n] = copy_a[row+1][c-n]
            copy_a[r+n][c-n:c+n] = copy_a[r+n][c-n+1:c+n+1]  # <-
            for row in range(r+n, r-n, -1):  # ↓
                copy_a[row][c+n] = copy_a[row-1][c+n]
            copy_a[r-n+1][c+n] = tmp

    # 3. 각 행의 최소값 찾기
    for row in copy_a:
        ans = min(ans, sum(row))

print(ans)



# 백준16935

# import sys
# from copy import deepcopy
# # input = sys.stdin.readline
# # 1번 연산 : 상하 반전
# # 2번 연산 : 좌우 반전
# # 3번 연산 : 오른쪽으로 90도 
# # 4번 연산 : 왼쪽으로 90 도
# # 5번 연산 -> A,B,C,D를 그룹으로 나누고 저장시키고 A + B, C + D식으로 진행하고 append
# # 5번 연산 : 1번그룹 -> 2번 그룹
# sys.stdin = open('./input.txt')
# def Operation(Board, Opr, N, M):
#     New_Board = deepcopy(Board)
#     Answer = []
#     if Opr == 1:
#         for exam in New_Board[::-1]:
#             Answer.append(exam)
#     elif Opr == 2:
#         for exam in New_Board:
#             Example = []
#             for sam in exam[::-1]:
#                 Example.append(sam)
#             Answer.append(Example)
#     elif Opr == 3:
#         Answer = list(map(list, zip(*New_Board[::-1])))
#     elif Opr == 4:
#         for i in New_Board:
#             Answer.append(i[::-1])
#         Answer = list(map(list, zip(*Answer)))
#     elif Opr == 5:
#         Dict = {'A': [], 'B': [] ,'C': [], 'D': []}
#         for dt in Dict:
#             for i in range(0, N, N,2):
#                 New = []
#                 for j in range(0, M, M/2):
#                     New.append(New_Board[i:j])
                
            
#     return Answer

# N, M, R = map(int, input().split())
# Board = [list(map(int, input().split())) for _ in range(N)]
# Opr = int(input())
# Answer = Operation(Board, Opr, N, M)
# for i in Answer:
#     print(*i)