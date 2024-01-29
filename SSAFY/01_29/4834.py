T = int(input())

for case in range(T):
    case += 1
    number_len = int(input())
    number_list = list(map(int, input().split())) 
    number_dict = dict.fromkeys(number_list,0)
    
    Max = 0
    max_count = 0
    for number in number_list:
        number_dict[number] += 1
        
    for key,value in number_dict.items():
        if max_count < value:
            max_count = value
            Max = key
        elif max_count == value:
            if Max < key:
                Max = key
        

    print(f'#{case} {Max} {max_count}')
