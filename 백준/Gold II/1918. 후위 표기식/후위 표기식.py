def posfix(List):
    isp = {'(':0, '*':2, '/':2, '+':1, '-':1} #스택 안에서의 우선순위
    top = -1
    stack  = [0]*len(List)
    postfix = ''
    for ch in List :
        if ch.isalnum() :
            postfix += ch
        elif ch == '(' :
            top += 1
            stack[top] = ch
        elif ch == ')' :
            while top > -1 and stack[top] != '(' :
                postfix += stack[top]
                top -= 1
            top -=1 # stack안의 '(' 제거
        elif ch in isp :  #연산자인경우
            while top > -1 and isp[stack[top]] >= isp[ch] :
                postfix += stack[top]
                top -= 1
            top += 1
            stack[top] = ch

    #stack에 남아 있는 연산자들 문자열에 붙이기
    while top > -1 :
        postfix += stack[top]
        top -= 1
    return postfix

List = input()
print(posfix(List))
