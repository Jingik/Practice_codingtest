T = int(input())

for case in range(T):
    case += 1
    number_len, case_len = map(int, input().split())
    number_list = list(map(int, input().split())) 
    
    Max = sum(number_list[:case_len])
    Min = sum(number_list[:case_len])
    for i in range(number_len-case_len + 1):
        if Max < sum(number_list[i:case_len + i]):
            Max = sum(number_list[i:case_len + i ])
        
        if Min > sum(number_list[i:case_len + i ]):
            Min = sum(number_list[i:case_len + i ])
                  
    result = Max - Min
    print(f'#{case} {result}')
