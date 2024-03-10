import sys
# sys.stdin = open("input.txt")
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().rstrip().split()))
stack = [[], [], [], []]

"""
무조건 stack 최상단 수보다 큰수를 삽입해야함
"""
check = True
for x in arr:
    for i in range(4):
        if not stack[i]:			# 스택이 비어있으면 삽입
            stack[i].append(x)
            break					# 나머지 스택에 대해선 볼 필요가 없으므로
        else:
            if stack[i][-1] < x:	# 오름차순으로 넣을 수 있는 경우에만
                stack[i].append(x)
                break
    else:
        check = False				# 숫자를 어느 스택에도 넣을 수 없으면
        break

if check:
    print("YES")
else:
    print("NO")
