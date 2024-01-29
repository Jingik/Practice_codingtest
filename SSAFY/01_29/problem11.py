############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
def get_final_position(N, matrix, move_list):
    pass
    # 여기에 코드를 작성하여 함수를 완성합니다.
    key = [(-1, 0), (1,0), (0,-1), (0,1)]
    cur_r, cur_c = 0, 0
    for r in range(N):
        for c in range(N):
            if matrix[r][c] == 1 :
                cur_r, cur_c = r, c
                break
        else:
            continue
        break
    for move in move_list:
        cur_r += key[move][0]
        cur_c += key[move][1]
        if cur_r < 0 or cur_c >= N or cur_c < 0 or cur_c>=N:
            return None
    return [cur_r, cur_c]
        

# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 
############## 테스트 코드 삭제 금지 #################
N = 3
matrix = [
    [1, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
] 
moves1 = [1, 1, 3]
print(get_final_position(N, matrix, moves1)) # [2, 1]

moves2 = [1, 2, 3, 3]
print(get_final_position(N, matrix, moves2)) # None
#####################################################
