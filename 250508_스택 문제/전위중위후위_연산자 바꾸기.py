infix = input("전위 후위로 바꿀 중위 연산식을 입력하세요.")

# 후위 전환
def infix_to_postfix(infix):
    operator = {'+':1, '-':1, '*':2, '/':2, '^':3}
    result = []
    stack = []

    for i in infix:
        if i.isalnum():
            result.append(i)
        elif i == '(':
            stack.append(i)
        elif i == ')':
            while stack and stack[-1] != '(':
                result.append(stack.pop())
            stack.pop()
        else:
            while (stack and stack[-1] != ("(") and operator.get(i,0) <= operator.get(stack[-1],0)):
                result.append(stack.pop())
            stack.append(i)

    while stack:
        result.append(stack.pop())

    return ''.join(result)

# 전위 전환
def infix_to_prefix(infix):
    operator = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    result = []
    stack = []

    # 중위식 뒤집기
    infix = infix[::-1]

    temp_infix = []
    for i in infix:
        if i == '(':
            temp_infix.append(')')
        elif i == ')':
            temp_infix.append('(')
        else:
            temp_infix.append(i)

    for i in temp_infix:
        if i.isalnum():
            result.append(i)
        elif i == '(':
            stack.append(i)
        elif i == ')':
            while stack and stack[-1] != '(':
                result.append(stack.pop())
            stack.pop()
        else:
            while (stack and stack[-1] != '(' and operator.get(i, 0) <= operator.get(stack[-1], 0)):
                result.append(stack.pop())
            stack.append(i)

    while stack:
        result.append(stack.pop())

    return ''.join(result)[::-1]


print(infix_to_postfix(infix))
print(infix_to_prefix(infix))






