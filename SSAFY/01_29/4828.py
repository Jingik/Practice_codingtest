T = int(input())

for case in range(T):
    case += 1
    number_len = int(input())
    number_list = list(map(int, input().split())) 
    
    Max = number_list[0]
    Min = number_list[0]
    for number in number_list:
        if Max < number:
            Max = number
        if Min > number:
            Min = number
    result = Max - Min
            
    print(f'#{case} {result}')
