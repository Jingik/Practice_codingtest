def check(check_map):
    
    for i in range(9):
        row_check = [0] * 9  
        col_check = [0] * 9
        for j in range(9):
            row_check[check_map[i][j] - 1] += 1
            col_check[check_map[j][i] - 1] += 1

        if all(count == 1 for count in row_check) != True:
            return False
        if all(count == 1 for count in col_check) != True:
            return False
        
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            subgrid_check = [0] * 9
            for x in range(3):
                for y in range(3):
                    subgrid_check[check_map[i + x][j + y] -1] += 1
            
            if all(count == 1 for count in subgrid_check) != True:
                return False
    
    return True


T = int(input())

for testcase in range(1, T + 1):
    sample = [list(map(int, input().split())) for _ in range(9)]
    if check(sample):
        result = 1
    else:
        result = 0

    print(f'#{testcase} {result}')
