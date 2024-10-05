# 입력 받기
N = int(input())
words = [input() for _ in range(N)]

# 알파벳의 가중치를 저장할 딕셔너리
alpha_weight = {}

# 각 단어에 대해 자릿수에 따른 알파벳 가중치 계산
for word in words:
    length = len(word)
    for i, char in enumerate(word):
        if char in alpha_weight:
            alpha_weight[char] += 10 ** (length - i - 1)
        else:
            alpha_weight[char] = 10 ** (length - i - 1)

# 가중치가 큰 순서대로 정렬
sorted_alpha = sorted(alpha_weight.items(), key=lambda x: -x[1])
# 숫자 할당 (9부터 0까지)
assigned_values = {}
number = 9
for char, _ in sorted_alpha:
    assigned_values[char] = number
    number -= 1

# 단어들을 숫자로 변환하여 합계 계산
total_sum = 0
for word in words:
    current_value = 0
    for char in word:
        current_value = current_value * 10 + assigned_values[char]
    total_sum += current_value

# 결과 출력
print(total_sum)
