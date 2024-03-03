import sys
input = sys.stdin.readline
Stack_Answer = []
Stack_term = []
Result = 0
for _ in range(int(input())):
    List = list(map(int, input().split()))
    if List[0] == 1:
        Stack_term.append(List[2])
        Stack_Answer.append(List[1])
    if Stack_term:
        score = Stack_term.pop()
        time = Stack_Answer.pop()
        score -= 1
        if score == 0:
            Result += time
        else:
            Stack_term.append(score)
            Stack_Answer.append(time)

print(Result)
            