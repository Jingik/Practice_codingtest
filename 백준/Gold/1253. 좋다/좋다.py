import sys
input = sys.stdin.readline

N = int(input())
Num_list = list(map(int, input().split()))
total_count = 0
Num_list.sort()

for num in range(N):
    left = 0
    right = N - 1
    while left < right:
        if left == num:
            left += 1
            continue
        if right == num:
            right -= 1
            continue
        current = Num_list[left] + Num_list[right]
        target = Num_list[num]
        if target < current:
            right -= 1
        elif target > current:
            left += 1
        else:
            total_count += 1
            break
print(total_count)    
    