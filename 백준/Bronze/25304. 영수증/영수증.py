T = int(input())
case = int(input())
result = 0
for _ in range(case):
    price, number = map(int, input().split())
    result += price * number
if result == T:
    print('Yes')
else:
    print('No')