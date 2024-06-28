import sys
input = sys.stdin.readline

Sentence = input().rstrip()
explosion_string = input().rstrip()

stack = []
ex_len = len(explosion_string)

for i in range(len(Sentence)):
    stack.append(Sentence[i])
    if ''.join(stack[-ex_len:]) == explosion_string:
        for _ in range(ex_len):
            stack.pop()

if stack:
    print(''.join(stack))
else:
    print('FRULA')