import sys
input = sys.stdin.readline
Stack_Answer = []
Stack_term = []
Result = 0
for _ in range(int(input())):
    List = list(map(int, input().split()))
    if len(List) > 1:
        if List[2] - 1 == 0:
            Result += List[1]
        else:
            Stack_term.append(List[2] - 1)
            Stack_Answer.append(List[1])
    else:
        if Stack_term :
            Stack_term[-1] -= 1
            if Stack_term[-1] == 0:
                Stack_term.pop()
                Result += Stack_Answer[-1]

print(Result)