import sys
input = sys.stdin.readline

n, c, w = map(int, input().split())
trees = [int(sys.stdin.readline()) for _ in range(n)]
max_money = 0

for i in range(1, max(trees) + 1):
    money = 0

    for j in trees:
        cnt, remain = divmod(j, i)

        if remain:
            expense = cnt * c

        else:
            expense = (cnt - 1) * c
            
        target = (cnt * w * i) - expense

        if target < 0:
            continue
        money += target

    if money >= max_money:
        max_money = money

print(max_money)