import sys
sys.stdin = open('./input.txt')

for case in range(1, 11):
    n = int(input())
    List = list(map(int, input().split()))
    result = 0
    lst = [-2, -1, 1, 2]
    
    for number in range(2, n-2):
        side_lst = []
        for j in lst:
            side_lst.append(List[number+j]) 
        if max(side_lst) >= List[number]:
            continue
        else:
            result += List[number] - max(side_lst) 
    print(f"#{case} {result}")