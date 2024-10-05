n = int(input())
words = [input() for _ in range(n)]

# 가중치 계산
weight = {}
for word in words:
    length = len(word)
    for index, val in enumerate(word):
        if val not in weight:
            weight[val] = 10 ** (length - index - 1)
        else:
            weight[val] += 10 ** (length - index - 1)

sorted_weight = sorted(weight.items(), key = lambda x : -x[1])
# 할당
assign = {}
number = 9
for key, val in sorted_weight:
    assign[key] = number
    number -= 1
    
total = 0
for word in words:
    current = 0
    for val in word:
        current = current * 10 + assign[val]
    total += current
print(total)