N, K = map(int, input().split())
number = input()

stack = []
to_remove = K  # 제거해야 할 숫자의 개수

for digit in number:
    # 스택이 비어 있지 않고, 스택의 최상단 숫자가 현재 숫자보다 작고, 제거할 수 있는 숫자가 남아있을 때
    while to_remove > 0 and stack and stack[-1] < digit:
        stack.pop()  # 스택의 최상단 숫자를 제거
        to_remove -= 1  # 제거할 숫자의 개수를 하나 줄임
    stack.append(digit)  # 현재 숫자를 스택에 추가

# 만약 제거할 숫자가 남아 있으면, 뒤에서부터 제거
result = stack[:N-K]

# 결과 출력
print(''.join(result))
