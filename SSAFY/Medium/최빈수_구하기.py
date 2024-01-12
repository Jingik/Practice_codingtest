T = int(input())

for i in range(1, T + 1):
    number = int(input())
    case = list(map(int, input().split()))
    counter = {}
    for value in case:
        try:
            counter[value] += 1
        except:
            counter[value] = 1

    for key, value in counter.items():
        if value == max(counter.values()):
            print(f'#{i} {key}')
            break