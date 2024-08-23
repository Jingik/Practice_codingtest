def postfix(List): #
    Speed = {"+": 1, "-": 1, "*": 2, "/": 2, "(" : 0}
    text = ""
    Stack = []
    for i in List:
        if i.isalnum():
            text += i
        else:
            if i == "(":
                Stack.append(i)
            elif i == ")":
                while len(Stack) and Stack[-1] != "(":
                    text += Stack.pop()
                Stack.pop()
            elif i in Speed:
                while len(Stack) and Speed[Stack[-1]] >= Speed[i]:
                    text += Stack.pop()
                Stack.append(i)

    while len(Stack) > 0:
        text += Stack.pop()
    return text

List = input()
print(postfix(List))
