import sys; input = sys.stdin.readline
### Case 1

# N = int(input())
# board = [list(map(int, input().split())) for _ in range(N)]
# final_max = 0
# start = board.pop(0)
# for i in range(6):
#     Max = 0
#     serach = start[i]
#     if i == 0 or i == 5:
#         Max += max(start[1:5])
#     elif i == 1 or i == 3:
#         new_start = start[:]
#         new_start.pop(1)
#         new_start.pop(2)
#         Max += max(new_start)
#     elif i == 2 or i == 4:
#         new_start = start[:]
#         new_start.pop(2)
#         new_start.pop(3)
#         Max += max(new_start)
    
#     for exam in board: # 각 주사위 별 최대값 더하기
#         Index = exam.index(serach)
#         if Index == 0:
#             Max += max(exam[1:5])
#             serach = exam[5] 
#         elif Index == 5:
#             Max += max(exam[1:5])
#             serach = exam[0]
            
#         elif Index == 1:
#             new_exam = exam[:]
#             new_exam.pop(1)
#             new_exam.pop(2)
#             Max += max(new_exam)
#             serach = exam[3]
            
#         elif Index == 3:
#             new_exam = exam[:]
#             new_exam.pop(1)
#             new_exam.pop(2)
#             Max += max(new_exam)
#             serach = exam[1]
            
            
#         elif Index == 2:
#             new_exam = exam[:]
#             new_exam.pop(2)
#             new_exam.pop(3)
#             Max += max(new_exam)
#             serach = exam[4]
#         elif Index == 4:
#             new_exam = exam[:]
#             new_exam.pop(2)
#             new_exam.pop(3)
#             Max += max(new_exam)
#             serach = exam[2]
            
#     if final_max < Max:
#         final_max = Max
# print(final_max)


### Case 2

N = int(input())
pair_num = { 0: 5, 1: 3, 2: 4, 3: 1, 4: 2, 5: 0 }
ans = 0
dice = [ list(map(int,input().split())) for _ in range(N) ]
first_dice = dice.pop(0)
for i in range(6): #
    s = 0
    tmp = [ 1,2,3,4,5,6 ]
    tmp.remove(first_dice[i])
    next = first_dice[pair_num[i]]
    tmp.remove(next)
    s+=max(tmp)

    for j in range(N-1):
        tmp = [ 1,2,3,4,5,6 ]
        tmp.remove(next)
        next = dice[j][pair_num[dice[j].index(next)]]
        tmp.remove(next)
        s+=max(tmp)
    
    ans = max(ans,s)

print(ans)
